def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    largest = float('-inf')
    second_largest = float('-inf')
    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None