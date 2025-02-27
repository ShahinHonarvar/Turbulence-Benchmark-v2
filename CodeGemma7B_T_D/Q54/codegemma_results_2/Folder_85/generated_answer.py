from math import sqrt

def all_right_truncatable_prime(tup):
    x = tup[94]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            truncatable = True
            num = i
            while num > 0:
                digit = num % 10
                num //= 10
                if digit % 2 == 0 or digit == 5 or digit == 0:
                    truncatable = False
                    break
            if truncatable:
                primes.append(i)
    primes.sort()
    return primes