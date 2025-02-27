def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(nums):
    primes = [num for num, i in zip(nums[69:81], range(69, 81)) if is_prime(num)]
    return sorted(primes) if primes else []