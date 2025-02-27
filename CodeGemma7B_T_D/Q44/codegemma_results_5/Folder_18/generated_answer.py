from math import sqrt

def composite_nums_between_indices(nums):
    composites = set()
    for i in range(25, 88):
        if nums[i] % 2 == 0:
            composites.add(nums[i])
            continue
        for j in range(3, int(sqrt(nums[i])) + 1, 2):
            if nums[i] % j == 0:
                composites.add(nums[i])
                break
    return composites