import math

def all_right_truncatable_prime(n):

    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    def get_right_truncatable_primes(x):
        primes = []
        for n in range(2, x):
            if is_prime(n):
                if all((is_prime(n // 10 ** (i + 1)) for i in range(len(str(n)) - 1))):
                    primes.append(n)
        return primes
    return sorted(get_right_truncatable_primes(n[73])[-1::-1])