def find_second_smallest_num(num_list):
    selected_nums = num_list[22:64]
    sorted_nums = sorted(selected_nums)
    if len(sorted_nums) < 2:
        return None
    else:
        return sorted_nums[1]