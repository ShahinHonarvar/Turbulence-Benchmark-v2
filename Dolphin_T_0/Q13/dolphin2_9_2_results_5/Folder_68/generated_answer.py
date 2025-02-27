def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    first = second = float('-inf')
    for i in range(9):
        if lst[i] > first:
            second = first
            first = lst[i]
        elif lst[i] > second and lst[i] != first:
            second = lst[i]
    return second if second != float('-inf') else None