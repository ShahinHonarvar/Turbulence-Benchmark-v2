def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    second_max = float('-inf')
    first_max = float('-inf')
    for num in lst[0:4]:
        if num > first_max:
            first_max, second_max = (num, first_max)
        elif first_max > num > second_max:
            second_max = num
    return None if second_max == float('-inf') else second_max