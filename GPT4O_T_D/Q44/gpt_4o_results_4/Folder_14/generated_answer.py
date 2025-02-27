def is_composite(num):
    if num < 4:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False

def composite_nums_between_indices(nums):
    if len(nums) <= 4:
        return set()
    return {num for num in nums[4:5] if is_composite(num)}