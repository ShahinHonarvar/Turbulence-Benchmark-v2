def find_second_largest_num(lst):
    if len(lst) < 37:
        return None
    sub_lst = lst[33:37]
    if len(sub_lst) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in sub_lst:
        if num > largest:
            second_largest, largest = (largest, num)
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None