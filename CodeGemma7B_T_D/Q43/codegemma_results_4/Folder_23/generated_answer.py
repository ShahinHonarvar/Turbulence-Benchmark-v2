def find_primes_between_indices(lst):
    nums = lst[20:49]
    primes = sorted([num for num in nums if is_prime(num)], reverse=True)
    return primes if primes else []

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True