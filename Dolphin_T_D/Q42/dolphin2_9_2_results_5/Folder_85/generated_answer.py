def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(lst):
    if not is_prime(lst[23]):
        for i in range(2, lst[23] + 1):
            if lst[23] % i == 0 and is_prime(i):
                return i
    else:
        return lst[23]