def find_second_smallest_num(lst):
    sublist = lst[35:50]
    unique_elements = list(set(sublist))
    if len(unique_elements) < 2:
        return None
    return sorted(unique_elements)[1]