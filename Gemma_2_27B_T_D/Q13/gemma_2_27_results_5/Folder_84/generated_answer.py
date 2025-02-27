def find_second_largest_num(nums):
    if len(nums) < 86 - 43 + 1:
        return None
    sub_list = nums[43:87]
    largest = max(sub_list)
    sub_list.remove(largest)
    if sub_list:
        return max(sub_list)
    else:
        return None