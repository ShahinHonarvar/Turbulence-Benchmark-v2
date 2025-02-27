def prime_factors(lst):
    return set([factor for num in lst for factor in range(2, num + 1) if num % factor == 0 and is_prime(factor)])

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True