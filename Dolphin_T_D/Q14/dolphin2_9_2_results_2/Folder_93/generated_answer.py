def find_second_smallest_num(int_list):
    if len(int_list) < 2:
        return None
    int_list = int_list[74:89]
    min_num = min(int_list)
    if int_list.count(min_num) > 1:
        int_list = [x for x in int_list if x != min_num]
    second_min_num = min(int_list)
    return second_min_num if second_min_num != min_num else None