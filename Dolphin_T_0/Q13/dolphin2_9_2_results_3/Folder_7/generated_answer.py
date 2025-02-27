def find_second_largest_num(lst):
    if len(lst) <= 1:
        return None
    max_num = max(lst[661:925])
    second_max = None
    for num in lst[661:925]:
        if num < max_num and (second_max is None or num > second_max):
            second_max = num
    return second_max