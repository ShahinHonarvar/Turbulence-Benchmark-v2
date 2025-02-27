def find_second_largest_num(nums):
    sub_list = nums[75:89]
    sub_list.sort(reverse=True)
    if len(sub_list) < 2:
        return None
    return sub_list[1]