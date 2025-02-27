def find_second_smallest_num(num_list):
    if not isinstance(num_list, list) or not all((isinstance(i, (int, float)) for i in num_list)):
        return None
    try:
        second_min = sorted(num_list[:8])[1]
    except IndexError:
        return None
    return second_min