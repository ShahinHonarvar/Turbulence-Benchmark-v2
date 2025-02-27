import re

def all_right_truncatable_prime(n):
    x = n[32]
    primes = []
    for num in range(3, x, 2):
        if all((n % d == 0 for d in range(3, int(str(num)[-1]) + 1, 2))):
            for d in range(int(str(num)[-1]) + 1, int(str(num)) + 1, 2):
                if num % d == 0:
                    break
            else:
                primes.append(num)
    return primes