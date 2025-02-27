def find_second_smallest_num(nums):
    if len(nums) < 76 or len(nums) < 37:
        return None
    sub_list = nums[37:77]
    sorted_list = sorted(sub_list)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]