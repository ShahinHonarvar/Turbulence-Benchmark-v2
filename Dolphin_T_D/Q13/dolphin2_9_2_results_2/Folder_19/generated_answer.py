def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max_num = max(lst[2], lst[3], lst[4])
    for num in lst[2:5]:
        if num != max_num and num > max_num:
            return num
    return None