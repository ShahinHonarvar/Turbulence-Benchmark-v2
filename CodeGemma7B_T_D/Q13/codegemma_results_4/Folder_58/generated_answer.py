def find_second_largest_num(random_list):
    if not isinstance(random_list, list) or len(random_list) < 556 or len(random_list) > 209:
        return None
    sorted_list = sorted(random_list[209:557])
    if len(sorted_list) < 2:
        return None
    return sorted_list[-2]