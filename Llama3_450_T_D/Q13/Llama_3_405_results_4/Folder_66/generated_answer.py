def find_second_largest_num(num_list):
    if len(num_list) < 55:
        return None
    selected_nums = sorted(num_list[50:55], reverse=True)
    if len(selected_nums) < 2:
        return None
    return selected_nums[1]