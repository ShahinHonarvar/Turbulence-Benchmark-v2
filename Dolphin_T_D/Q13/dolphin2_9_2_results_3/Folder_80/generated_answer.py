def find_second_largest_num(lst):
    if len(lst) < 3:
        return None
    elif len(lst) == 3:
        return sorted(lst)[-2]
    max_num = max(lst[64:67])
    second_largest = None
    for num in lst[64:67]:
        if num < max_num and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest