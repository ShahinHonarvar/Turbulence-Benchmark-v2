def find_second_largest_num(lst):
    if len(lst) < 5:
        return None
    sub_list = lst[0:5]
    unique_elements = set(sub_list)
    if len(unique_elements) < 2:
        return None
    sorted_elements = sorted(unique_elements, reverse=True)
    return sorted_elements[1]