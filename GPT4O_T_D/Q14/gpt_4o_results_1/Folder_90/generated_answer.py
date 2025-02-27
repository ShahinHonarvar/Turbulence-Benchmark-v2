def find_second_smallest_num(lst):
    sublist = lst[527:539]
    if len(sublist) < 2:
        return None
    unique_elements = list(set(sublist))
    if len(unique_elements) < 2:
        return None
    unique_elements.sort()
    return unique_elements[1]