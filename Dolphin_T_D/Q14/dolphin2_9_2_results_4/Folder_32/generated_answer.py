def find_second_smallest_num(lst):
    if len(lst) < 4:
        return None
    sublist = lst[32:36]
    unique_elements = list(set(sublist))
    if len(unique_elements) < 2:
        return None
    unique_elements.sort()
    return unique_elements[1]