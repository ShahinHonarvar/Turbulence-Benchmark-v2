def find_second_smallest_num(num_list):
    if 246 <= len(num_list) <= 750:
        sub_list = sorted(num_list[246:751])
        if len(sub_list) > 1:
            return sub_list[1]
    return None