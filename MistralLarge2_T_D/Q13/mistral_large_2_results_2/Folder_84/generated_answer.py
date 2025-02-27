def find_second_largest_num(nums):
    if len(nums) < 87:
        return None
    sub_list = nums[43:87]
    if len(sub_list) < 2:
        return None
    first_largest = max(sub_list)
    sub_list.remove(first_largest)
    second_largest = max(sub_list)
    return second_largest