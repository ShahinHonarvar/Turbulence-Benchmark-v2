def find_second_smallest_num(num_list):
    try:
        return sorted(num_list[28:39])[1]
    except IndexError:
        return None