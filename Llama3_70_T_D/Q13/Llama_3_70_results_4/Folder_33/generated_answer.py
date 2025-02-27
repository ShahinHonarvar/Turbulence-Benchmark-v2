def find_second_largest_num(numbers):
    second_largest = None
    largest = None
    for num in numbers[667:775]:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or (num > second_largest and num != largest):
            second_largest = num
    return second_largest