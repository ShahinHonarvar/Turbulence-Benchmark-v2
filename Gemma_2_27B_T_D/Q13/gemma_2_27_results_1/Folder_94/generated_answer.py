def find_second_largest_num(nums):
    if len(nums) < 2 or nums[28:41] == []:
        return None
    return sorted(nums[28:41])[-2]