def find_second_smallest_num(lst):
    if 94 < len(lst) < 75:
        return None
    sublist = lst[75:95]
    unique_chars = list(set(sublist))
    if len(unique_chars) < 2:
        return None
    unique_chars.sort()
    return unique_chars[1]