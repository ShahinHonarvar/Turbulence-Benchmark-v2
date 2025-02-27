def find_second_smallest_num(num_list):
    if len(num_list) < 98 or not all((isinstance(x, (int, float)) for x in num_list)):
        return None
    selected_nums = sorted(num_list[59:98])
    if len(selected_nums) < 2:
        return None
    return selected_nums[1]