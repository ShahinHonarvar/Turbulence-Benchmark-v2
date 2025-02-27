def find_second_smallest_num(num_list):
    if len(num_list[639:976]) < 2:
        return None
    else:
        sorted_nums = sorted(set(num_list[639:976]))
        return sorted_nums[1]