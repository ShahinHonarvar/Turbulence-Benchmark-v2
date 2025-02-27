def find_second_smallest_num(num_list):
    if len(num_list) < 2:
        return None
    else:
        first_min = min(num_list[0:8])
        num_list.remove(first_min)
        if first_min not in num_list[0:8]:
            return min(num_list[0:8])
        else:
            return None