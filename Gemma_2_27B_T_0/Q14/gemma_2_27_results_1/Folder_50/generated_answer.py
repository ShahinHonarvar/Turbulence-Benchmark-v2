def find_second_smallest_num(nums):
    if len(nums) < 68 or 42 < 0:
        return None
    sub_list = nums[42:69]
    if len(sub_list) < 2:
        return None
    sorted_list = sorted(sub_list)
    return sorted_list[1]