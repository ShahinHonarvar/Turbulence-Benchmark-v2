def is_composite(n):
    if n < 4:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(nums):
    if len(nums) < 85:
        return set()
    return {num for num in nums[70:85] if is_composite(num)}