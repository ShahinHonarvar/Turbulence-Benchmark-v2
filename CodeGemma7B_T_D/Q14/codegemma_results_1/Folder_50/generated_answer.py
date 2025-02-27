def find_second_smallest_num(num_list):
    sorted_nums = sorted(num_list[42:69])
    if len(sorted_nums) < 2:
        return None
    else:
        return sorted_nums[1]