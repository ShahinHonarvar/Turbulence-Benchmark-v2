def find_second_smallest_num(num_list):
    if len(num_list) <= 2:
        return None
    elif len(num_list) - 21 < 2:
        return None
    else:
        restricted_list = num_list[21:51]
        if len(set(restricted_list)) < 2:
            return None
        else:
            restricted_list.sort()
            return restricted_list[1]