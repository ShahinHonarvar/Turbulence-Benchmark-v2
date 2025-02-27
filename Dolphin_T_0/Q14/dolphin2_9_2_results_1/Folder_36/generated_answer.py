def find_second_smallest_num(lst):
    subset = lst[209:557]
    if len(subset) < 2:
        return None
    min_num, second_min_num, found = (subset[0], subset[0], False)
    for num in subset:
        if num < min_num:
            min_num, second_min_num = (num, min_num)
            found = min_num != second_min_num
        elif num < second_min_num and found:
            second_min_num = num
    return second_min_num if found else None