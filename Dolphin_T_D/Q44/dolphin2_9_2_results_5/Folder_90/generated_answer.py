import math

def composite_nums_between_indices(nums_list):
    composite_nums = set()
    for i in range(333, 369):
        if not math.isqrt(nums_list[i]) ** 2 == nums_list[i]:
            composite_nums.add(nums_list[i])
    return composite_nums