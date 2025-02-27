def find_second_largest_num(nums):
    if len(nums) < 988 or len(nums) < 687:
        return None
    sub_list = nums[686:988]
    sub_list.sort()
    if len(sub_list) >= 2:
        return sub_list[-2]
    else:
        return None