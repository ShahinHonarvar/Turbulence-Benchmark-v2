def find_second_largest_num(num_list):
    if len(num_list) < 2:
        return None
    elif len(num_list[75:89]) < 2:
        return None
    else:
        nums = num_list[75:89]
        first = max(nums)
        nums.remove(first)
        return max(nums)