def find_second_largest_num(num_list):
    if len(num_list) < 2:
        return None
    first = max(num_list)
    num_list.remove(first)
    second = max(num_list)
    return second if second != first else None