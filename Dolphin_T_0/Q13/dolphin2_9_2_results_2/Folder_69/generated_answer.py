def find_second_largest_num(lst):
    if len(lst) < 3:
        return None
    largest = float('-inf')
    second_largest = float('-inf')
    for i in range(32, 36):
        if i >= len(lst):
            return None
        num = lst[i]
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    return second_largest