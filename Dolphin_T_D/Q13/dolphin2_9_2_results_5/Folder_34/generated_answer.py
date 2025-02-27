def find_second_largest_num(lst):
    second_largest = None
    largest = None
    for num in lst[16:62]:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif largest and num > second_largest:
            second_largest = num
    return second_largest