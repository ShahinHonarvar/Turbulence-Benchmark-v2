def find_second_largest_num(num_list):
    try:
        return sorted(num_list[29:52])[-2]
    except IndexError:
        return None