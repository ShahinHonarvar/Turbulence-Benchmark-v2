def is_composite(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False

def composite_nums_between_indices(nums):
    return {num for i, num in enumerate(nums[40:201], start=40) if is_composite(num)}