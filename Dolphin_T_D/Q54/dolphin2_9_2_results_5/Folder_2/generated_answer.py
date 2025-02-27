import math

def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2):
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = numbers[618]
    primes = []
    for n in range(2, x):
        if is_prime(n):
            truncations = [int(str(n)[::-1][i:]) for i in range(1, len(str(n))) if int(str(n)[::-1][i:]) != n]
            for t in truncations:
                if not is_prime(t):
                    break
            else:
                primes.append(n)
    return sorted(primes)