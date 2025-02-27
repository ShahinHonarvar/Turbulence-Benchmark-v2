from math import sqrt

def composite_nums_between_indices(nums):
    for i in range(64, 67):
        num = nums[i]
        if num <= 1:
            continue
        is_composite = False
        for j in range(2, int(sqrt(num)) + 1):
            if num % j == 0:
                is_composite = True
                break
        if is_composite:
            return {num}
    return set()