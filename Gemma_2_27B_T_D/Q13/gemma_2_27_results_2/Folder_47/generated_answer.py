def find_second_largest_num(nums):
    sub_list = nums[37:77]
    if len(sub_list) < 2:
        return None
    largest = max(sub_list)
    sub_list.remove(largest)
    return max(sub_list)