def find_second_largest_num(num_list):
    if 533 <= len(num_list) <= 605:
        num_list = num_list[533:606]
        if len(num_list) == 0:
            return None
        elif len(num_list) == 1:
            return None
        else:
            num_list = sorted(list(set(num_list)), reverse=True)
            return num_list[1]
    else:
        return None