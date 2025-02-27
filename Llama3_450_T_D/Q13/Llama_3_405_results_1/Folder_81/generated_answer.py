def find_second_largest_num(num_list):
    if len(num_list) < 101:
        return None
    nums = sorted(num_list[10:101])
    if len(nums) < 2:
        return None
    return nums[-2]