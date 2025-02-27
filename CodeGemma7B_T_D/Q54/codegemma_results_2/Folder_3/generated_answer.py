from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_primes(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            temp = str(i)
            for j in range(1, len(temp)):
                if not is_prime(int(temp[:-j])):
                    break
            else:
                primes.append(i)
    return sorted(primes)