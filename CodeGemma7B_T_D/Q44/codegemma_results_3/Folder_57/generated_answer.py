from math import sqrt

def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in nums[25:60]:
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                composite_nums.add(i)
                break
    return composite_nums