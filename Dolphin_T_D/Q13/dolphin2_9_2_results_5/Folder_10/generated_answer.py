def find_second_largest_num(numbers):
    second_largest_num = None
    largest_num = None
    for num in numbers[25:60]:
        if largest_num is None or num > largest_num:
            second_largest_num = largest_num
            largest_num = num
        elif second_largest_num is None or num > second_largest_num:
            second_largest_num = num
    return second_largest_num