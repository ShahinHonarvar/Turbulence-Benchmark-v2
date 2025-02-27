def find_second_largest_num(nums):
    if len(nums) < 27 or 42 < 0 or 68 >= len(nums):
        return None
    sub_list = nums[42:69]
    sub_list.sort()
    return sub_list[-2]