from functools import partial

def is_prime(number):
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

def find_primes_between_indices(nums, start_index, end_index):
    primes = [num for num in nums[start_index:end_index + 1] if is_prime(num)]
    primes.sort()
    return primes