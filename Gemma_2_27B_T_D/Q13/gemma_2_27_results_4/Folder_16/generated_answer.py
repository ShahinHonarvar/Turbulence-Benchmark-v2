def find_second_largest_num(nums):
    if 36 >= len(nums) - 1:
        return None
    sub_list = nums[33:37]
    sub_list.sort()
    return sub_list[-2]