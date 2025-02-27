def find_second_smallest_num(num_list):
    if 661 < len(num_list) <= 924:
        sub_list = num_list[661:925]
        sub_list.sort()
        return sub_list[1] if len(sub_list) > 1 else None
    else:
        return None