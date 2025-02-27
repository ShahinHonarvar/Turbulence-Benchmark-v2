def find_second_largest_num(lst):
    if len(lst) < 6:
        return None
    sub_lst = lst[:6]
    first_largest = second_largest = float('-inf')
    for num in sub_lst:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None