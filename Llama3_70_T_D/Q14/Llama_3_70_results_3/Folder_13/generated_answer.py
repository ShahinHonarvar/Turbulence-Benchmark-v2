def find_second_smallest_num(nums):
    if len(nums) < 33:
        return None
    sub_list = sorted(nums[28:33])
    if len(sub_list) < 2 or sub_list[0] == sub_list[1]:
        return None
    return sub_list[1]