def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max_num = max(lst[0], lst[1])
    second_max = min(lst[0], lst[1])
    for i in range(2, len(lst)):
        if lst[i] > max_num:
            second_max = max_num
            max_num = lst[i]
        elif lst[i] > second_max and lst[i] < max_num:
            second_max = lst[i]
    if second_max == max_num:
        return None
    return second_max