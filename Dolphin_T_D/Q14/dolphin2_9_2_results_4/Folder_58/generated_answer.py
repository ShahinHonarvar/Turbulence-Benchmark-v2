def find_second_smallest_num(nums):
    subset_nums = nums[310:370]
    if len(subset_nums) < 2:
        return None
    subset_nums.sort()
    return subset_nums[1]