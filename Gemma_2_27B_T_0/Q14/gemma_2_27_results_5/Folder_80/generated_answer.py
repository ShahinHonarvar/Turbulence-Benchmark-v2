def find_second_smallest_num(nums):
    if len(nums) < 87 or 30 < len(nums):
        return None
    sub_list = nums[30:88]
    sorted_list = sorted(sub_list)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]