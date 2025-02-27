def find_second_largest_num(lst):
    if 43 < len(lst) <= 86:
        part = lst[43:87]
        if len(part) > 1:
            max_value = max(part)
            part.remove(max_value)
            second_max = max(part)
            return second_max
    return None