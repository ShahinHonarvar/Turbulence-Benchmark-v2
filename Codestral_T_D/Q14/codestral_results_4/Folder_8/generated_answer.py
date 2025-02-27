def find_second_smallest_num(num_list):
    valid_nums = sorted(num_list[56:67])
    if len(valid_nums) > 1:
        return valid_nums[1]
    else:
        return None