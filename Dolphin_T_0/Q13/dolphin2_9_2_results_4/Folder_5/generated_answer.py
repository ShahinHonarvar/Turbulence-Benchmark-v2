def find_second_largest_num(lst):
    if len(lst) == 0:
        return 'None'
    if len(lst) == 1:
        return 'None'
    largest = max(lst[8:10])
    second_largest = float('-inf')
    for x in lst[8:10]:
        if x != largest and x > second_largest:
            second_largest = x
    if second_largest == float('-inf'):
        return 'None'
    return second_largest