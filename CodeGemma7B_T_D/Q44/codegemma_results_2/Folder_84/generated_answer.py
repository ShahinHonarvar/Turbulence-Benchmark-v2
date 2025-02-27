import math

def composite_nums_between_indices(list_of_nums):
    composite_nums = set()
    for i in range(30, 49):
        if list_of_nums[i] not in range(2, int(math.sqrt(list_of_nums[i])) + 1):
            composite_nums.add(list_of_nums[i])
    return composite_nums