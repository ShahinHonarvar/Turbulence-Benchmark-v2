def find_second_smallest_num(nums):
    target_nums = nums[43:52]
    if len(target_nums) < 2:
        return None
    target_nums.sort()
    return target_nums[1]