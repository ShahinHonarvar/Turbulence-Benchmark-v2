def find_second_largest_num(nums):
    if 62 > len(nums) or 78 > len(nums):
        return 'None'
    subset_nums = nums[62:79]
    if len(set(subset_nums)) < 2:
        return 'None'
    subset_nums.sort()
    return subset_nums[-2]