def find_second_smallest_num(num_list):
    to_search = num_list[34:56]
    if len(to_search) < 2:
        return None
    first_min = min(to_search)
    to_search.remove(first_min)
    second_min = min(to_search)
    return second_min if second_min else None