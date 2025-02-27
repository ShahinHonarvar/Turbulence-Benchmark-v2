def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    largest = float('-inf')
    second_largest = float('-inf')
    for i in range(0, 10):
        if lst[i] > largest:
            second_largest = largest
            largest = lst[i]
        elif lst[i] != largest and lst[i] > second_largest:
            second_largest = lst[i]
    if second_largest == float('-inf'):
        return None
    else:
        return second_largest