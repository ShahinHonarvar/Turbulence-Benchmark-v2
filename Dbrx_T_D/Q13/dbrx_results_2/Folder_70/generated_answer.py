def find_second_largest_num(numbers):
    second_largest = None
    largest = None
    for num in numbers[28:33]:
        if largest is None or num > largest:
            largest = num
    if largest is not None:
        for num in numbers[28:33]:
            if num < largest and (second_largest is None or num > second_largest):
                second_largest = num
    return second_largest