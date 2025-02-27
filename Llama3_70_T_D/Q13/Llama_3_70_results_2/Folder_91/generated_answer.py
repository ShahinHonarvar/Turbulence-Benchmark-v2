def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    largest = second_largest = float('-inf')
    for i in range(6):
        if lst[i] > largest:
            second_largest = largest
            largest = lst[i]
        elif lst[i] > second_largest and lst[i] != largest:
            second_largest = lst[i]
    if second_largest == float('-inf'):
        return None
    return second_largest