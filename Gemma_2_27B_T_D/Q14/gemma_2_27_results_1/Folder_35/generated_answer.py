def find_second_smallest_num(nums):
    if len(nums) < 25:
        return None
    sub_list = nums[15:40]
    sorted_list = sorted(sub_list)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]