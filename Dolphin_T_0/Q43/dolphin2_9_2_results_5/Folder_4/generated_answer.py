def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(nums):
    return sorted([nums[i] for i in range(24, 84) if is_prime(nums[i])])