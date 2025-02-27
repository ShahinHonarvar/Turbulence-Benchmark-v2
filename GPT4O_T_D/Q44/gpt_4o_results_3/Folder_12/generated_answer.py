def is_composite(n):
    if n <= 3:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(nums):
    if len(nums) < 52:
        return set()
    return {nums[i] for i in range(51, min(87, len(nums))) if is_composite(nums[i])}