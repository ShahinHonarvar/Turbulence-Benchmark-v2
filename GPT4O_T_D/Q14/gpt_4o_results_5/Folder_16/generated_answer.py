def find_second_smallest_num(lst):
    sub_lst = lst[66:78]
    if len(sub_lst) < 2:
        return None
    unique_elements = list(set(sub_lst))
    unique_elements.sort()
    return unique_elements[1] if len(unique_elements) > 1 else None