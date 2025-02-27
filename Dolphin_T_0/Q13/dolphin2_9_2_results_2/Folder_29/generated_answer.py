def find_second_largest_num(num_list):
    sub_list = num_list[59:98] if 59 <= len(num_list) <= 97 else None
    if sub_list:
        sorted_sub_list = sorted(sub_list)
        if len(sorted_sub_list) > 1:
            return sorted_sub_list[-2]
    return None