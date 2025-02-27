def find_second_largest_num(numbers):
    second_largest = None
    for num in numbers[10:101]:
        if second_largest is None or num > second_largest:
            if second_largest is not None:
                second_largest_prev = second_largest
            second_largest = num
        elif second_largest is not None and num < second_largest and (second_largest_prev is None or num > second_largest_prev):
            second_largest_prev = second_largest
    return second_largest_prev