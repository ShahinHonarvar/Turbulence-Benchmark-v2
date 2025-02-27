def find_second_largest_num(nums):
    if len(nums) < 78 or len(nums) < 62:
        return None
    sub_list = nums[62:79]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]