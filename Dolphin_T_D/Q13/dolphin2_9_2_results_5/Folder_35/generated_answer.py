def find_second_largest_num(lst):
    if len(lst) < 5:
        return None
    subset = lst[30:48]
    largest = second_largest = float('-inf')
    for x in subset:
        if x > largest:
            second_largest = largest
            largest = x
        elif x > second_largest:
            second_largest = x
    if second_largest == float('-inf'):
        return None
    return second_largest