def find_second_largest_num(l):
    if len(l) < 2:
        return None
    max_num = max(l[0], l[1])
    second_max = min(l[0], l[1])
    for i in l[2:]:
        if i > max_num:
            second_max = max_num
            max_num = i
        elif i > second_max and i < max_num:
            second_max = i
    if second_max == max(l[0], l[1]):
        return None
    return second_max