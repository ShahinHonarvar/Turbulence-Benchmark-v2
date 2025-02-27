def find_second_smallest_num(a_list):
    if len(a_list) < 3:
        return None
    return sorted(a_list[0:3])[1]