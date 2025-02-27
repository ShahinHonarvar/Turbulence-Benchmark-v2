def find_second_largest_num(input_list):
    if 75 <= len(input_list) - 1 <= 88:
        sub_list = input_list[75:89]
    else:
        return None
    max_val = max(sub_list)
    sub_list.remove(max_val)
    if sub_list:
        return max(sub_list)
    else:
        return None