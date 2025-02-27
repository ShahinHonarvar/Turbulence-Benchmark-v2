from math import sqrt

def find_primes_between_indices(list):
    prime_nums = []
    for num in list[13:29 + 1]:
        if is_prime(num):
            prime_nums.append(num)
    prime_nums.sort(reverse=True)
    return prime_nums

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True