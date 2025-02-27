def find_second_smallest_num(num_list):
    if len(num_list) < 80:
        return None
    selected_nums = sorted(num_list[29:80])
    if len(selected_nums) < 2:
        return None
    return selected_nums[1]