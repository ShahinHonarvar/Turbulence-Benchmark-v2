def find_second_smallest_num(num_list):
    if len(num_list) < 29:
        return None
    selected_nums = num_list[28:33]
    sorted_nums = sorted(selected_nums)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]