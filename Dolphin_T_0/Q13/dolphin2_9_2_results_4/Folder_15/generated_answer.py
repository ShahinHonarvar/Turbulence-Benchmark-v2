def find_second_largest_num(lst):
    if not lst or len(lst) < 2:
        return None
    max_num = max(lst[0:4])
    second_max = None
    for num in lst[0:4]:
        if num != max_num and (second_max is None or num > second_max):
            second_max = num
    return second_max