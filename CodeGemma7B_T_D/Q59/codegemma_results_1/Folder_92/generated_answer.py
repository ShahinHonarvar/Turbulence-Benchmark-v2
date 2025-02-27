import math

def all_left_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def get_truncated_primes(num):
        truncated_primes = []
        for i in range(1, num + 1):
            if is_prime(i):
                truncated_num = i
                while truncated_num > 0:
                    if not is_prime(truncated_num):
                        break
                    truncated_primes.append(i)
                    truncated_num //= 10
        return truncated_primes
    limit = x[7]
    primes = get_truncated_primes(limit)
    return sorted(primes)