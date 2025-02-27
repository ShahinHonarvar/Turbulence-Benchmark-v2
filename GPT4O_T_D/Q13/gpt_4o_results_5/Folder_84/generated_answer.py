def find_second_largest_num(nums):
    if len(nums) < 87:
        return None
    sub_list = nums[43:87]
    if len(sub_list) < 2:
        return None
    first = second = float('-inf')
    for num in sub_list:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    if second == float('-inf'):
        return None
    return second