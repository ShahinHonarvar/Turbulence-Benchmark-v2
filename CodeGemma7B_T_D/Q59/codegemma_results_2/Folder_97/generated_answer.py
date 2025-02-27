from math import sqrt

def is_prime(p):
    if p < 2:
        return False
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True

def all_left_truncatable_prime(x):
    truncatable_primes = []
    for i in range(2, x):
        str_i = str(i)
        if '0' in str_i:
            continue
        if is_prime(i):
            truncatable = True
            for j in range(1, len(str_i)):
                if not is_prime(int(str_i[j:])):
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.append(i)
    return sorted(truncatable_primes)