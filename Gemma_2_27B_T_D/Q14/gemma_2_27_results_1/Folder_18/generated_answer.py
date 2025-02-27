def find_second_smallest_num(nums):
    if len(nums) < 49 or 30 < 0 or 48 >= len(nums):
        return None
    sub_list = nums[30:49]
    sorted_list = sorted(sub_list)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]