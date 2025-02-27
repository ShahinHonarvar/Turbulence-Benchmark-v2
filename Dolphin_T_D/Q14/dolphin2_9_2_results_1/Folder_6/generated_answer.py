def find_second_smallest_num(my_list):
    if not any(my_list[29:80]):
        return None
    else:
        return sorted(my_list[29:80])[1]