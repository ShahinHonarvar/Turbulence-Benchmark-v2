def composite_nums_between_indices(nums):
    return set(filter(lambda x: x > 1 and x % 2 != 0 and (x % 3 != 0) and (x % 5 != 0), nums[56:67]))