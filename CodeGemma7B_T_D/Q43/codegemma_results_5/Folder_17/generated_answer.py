def find_primes_between_indices(nums):
    return sorted([n for n in nums[15:49] if is_prime(n)], reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True