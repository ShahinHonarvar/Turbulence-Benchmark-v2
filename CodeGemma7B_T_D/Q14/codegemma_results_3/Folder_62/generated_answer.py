def find_second_smallest_num(num_list):
    if len(num_list) <= 10 or len(num_list) > 66:
        raise ValueError('The list should have a length between 10 and 66, inclusive')
    sorted_nums = sorted(num_list[10:67])
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]