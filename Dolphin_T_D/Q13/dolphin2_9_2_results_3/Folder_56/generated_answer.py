def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max_num = max(lst[0], lst[1])
    for num in lst[2:]:
        if num == max_num:
            continue
        if num > max_num:
            return max_num
        max_num = num
    return None