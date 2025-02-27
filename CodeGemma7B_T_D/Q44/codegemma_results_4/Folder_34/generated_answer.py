from math import sqrt

def composite_nums_between_indices(nums):
    comp_nums = set()
    for num in nums[70:201]:
        if num > 1:
            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0:
                    comp_nums.add(num)
    return comp_nums or set()