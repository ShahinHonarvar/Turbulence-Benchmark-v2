def find_second_largest_num(num_list):
    if len(num_list) < 79:
        return None
    nums = sorted(num_list[62:79])
    if len(nums) < 2:
        return None
    return nums[-2]