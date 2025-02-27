def find_second_largest_num(num_list):
    valid_nums = num_list[12:93]
    if not valid_nums:
        return None
    valid_nums.remove(max(valid_nums))
    return max(valid_nums)