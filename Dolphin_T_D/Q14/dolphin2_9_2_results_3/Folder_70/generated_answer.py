def find_second_smallest_num(num_list):
    if not num_list:
        return None
    try:
        sub_list = num_list[35:50]
        if len(sub_list) < 2:
            return None
        first_min = min(sub_list)
        sub_list.remove(first_min)
        second_min = min(sub_list)
        return second_min
    except IndexError:
        return None