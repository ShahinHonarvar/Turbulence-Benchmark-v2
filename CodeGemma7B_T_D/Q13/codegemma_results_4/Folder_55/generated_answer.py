def find_second_largest_num(lst):
    if not lst or len(lst) < 3:
        return None
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    second_largest = None
    for num in lst:
        if num > second_largest and num != largest:
            second_largest = num
    return second_largest