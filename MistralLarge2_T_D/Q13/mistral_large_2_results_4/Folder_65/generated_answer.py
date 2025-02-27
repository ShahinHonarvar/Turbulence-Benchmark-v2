def find_second_largest_num(nums):
    if len(nums) < 99:
        return None
    sub_list = nums[56:99]
    if len(sub_list) < 2:
        return None
    max_num = max(sub_list)
    sub_list.remove(max_num)
    second_max_num = max(sub_list)
    return second_max_num