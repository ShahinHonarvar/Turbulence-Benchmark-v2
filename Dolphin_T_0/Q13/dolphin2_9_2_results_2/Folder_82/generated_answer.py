def find_second_largest_num(lst):
    if len(lst) == 0 or len(lst) < 200:
        return None
    sublist = lst[20:201]
    largest = second_largest = float('-inf')
    for num in sublist:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    if largest == float('-inf'):
        return None
    return second_largest