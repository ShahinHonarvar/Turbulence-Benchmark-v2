def find_second_largest_num(num_list):
    if len(num_list) < 67:
        return None
    nums = sorted(num_list[10:67])
    if len(nums) < 2:
        return None
    return nums[-2]