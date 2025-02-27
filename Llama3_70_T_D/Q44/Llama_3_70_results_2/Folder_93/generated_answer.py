def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_composite(n):
    return not is_prime(n)

def composite_nums_between_indices(nums):
    start_idx = 23
    end_idx = 43
    if end_idx >= len(nums):
        end_idx = len(nums) - 1
    if start_idx > end_idx:
        return set()
    return set((num for num in nums[start_idx:end_idx + 1] if is_composite(num)))