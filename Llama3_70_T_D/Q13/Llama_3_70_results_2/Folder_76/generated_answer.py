def find_second_largest_num(lst):
    slice_lst = lst[686:988]
    largest = None
    second_largest = None
    for num in slice_lst:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or num > second_largest:
            second_largest = num
    return second_largest