def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) < 33 or len(nums) > 36:
        return None
    else:
        new_list = nums[32:37]
        new_list.sort()
        return new_list[1]