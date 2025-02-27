def find_second_smallest_num(nums):
    if len(nums) < 98:
        return None
    sub_list = sorted(nums[59:98])
    if len(sub_list) < 2:
        return None
    return sub_list[1]