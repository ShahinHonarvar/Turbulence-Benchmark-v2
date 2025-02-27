from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_primes(num_list, index):
    x = num_list[index]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            is_truncatable = True
            n = i
            while n > 0:
                if not is_prime(n):
                    is_truncatable = False
                    break
                n //= 10
            if is_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)

def all_right_truncatable_prime(num_tuple):
    return right_truncatable_primes(num_tuple, 54)