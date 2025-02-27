def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    largest = second_largest = float('-inf')
    for i in range(5):
        if lst[i] > largest:
            second_largest = largest
            largest = lst[i]
        elif lst[i] > second_largest and lst[i] != largest:
            second_largest = lst[i]
    return second_largest if second_largest != float('-inf') else None