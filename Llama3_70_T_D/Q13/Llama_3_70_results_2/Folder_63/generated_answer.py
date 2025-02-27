def find_second_largest_num(lst):
    second_largest = None
    largest = None
    for num in lst[22:89]:
        if largest == None or num > largest:
            second_largest = largest
            largest = num
        elif num < largest and (second_largest == None or num > second_largest):
            second_largest = num
    return second_largest