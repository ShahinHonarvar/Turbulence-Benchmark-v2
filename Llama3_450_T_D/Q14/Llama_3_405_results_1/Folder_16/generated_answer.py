def find_second_smallest_num(nums):
    specific_nums = nums[66:78]
    if len(specific_nums) < 2:
        return None
    else:
        specific_nums.sort()
        return specific_nums[1]