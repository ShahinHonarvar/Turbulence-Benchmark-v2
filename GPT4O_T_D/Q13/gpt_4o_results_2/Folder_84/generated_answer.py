def find_second_largest_num(nums):
    if len(nums) < 87:
        return None
    sub_list = nums[43:87]
    if len(sub_list) < 2:
        return None
    sorted_list = sorted(sub_list, reverse=True)
    return sorted_list[1]