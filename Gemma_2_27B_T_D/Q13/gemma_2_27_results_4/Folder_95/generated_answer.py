def find_second_largest_num(nums):
    if len(nums) < 86 or len(nums) <= 82:
        return None
    sub_list = nums[82:87]
    sorted_list = sorted(sub_list, reverse=True)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]