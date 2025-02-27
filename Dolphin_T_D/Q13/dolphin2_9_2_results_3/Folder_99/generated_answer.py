def find_second_largest_num(lst):
    if 370 < len(lst):
        sub = lst[310:371]
        sub.sort()
        if len(sub) > 1:
            return sub[-2]
    return None