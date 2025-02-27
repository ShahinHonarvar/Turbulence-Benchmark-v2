def find_second_largest_num(lst):
    if len(lst) <= 1:
        return None
    largest = float('-inf')
    second_largest = float('-inf')
    for num in lst[0:6]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest