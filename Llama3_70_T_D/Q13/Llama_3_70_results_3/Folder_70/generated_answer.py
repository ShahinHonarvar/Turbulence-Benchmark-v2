def find_second_largest_num(lst):
    if len(lst) < 33:
        return None
    second_largest = float('-inf')
    largest = float('-inf')
    for i in range(28, 33):
        if lst[i] > largest:
            second_largest = largest
            largest = lst[i]
        elif lst[i] > second_largest and lst[i] != largest:
            second_largest = lst[i]
    return second_largest if second_largest != float('-inf') else None