def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(nums):
    if len(nums) < 25 or not nums[19:].count(is_prime(nums[19])) == 0:
        return []
    return sorted(set((num for num in nums[20:26] if is_prime(num))), reverse=True)