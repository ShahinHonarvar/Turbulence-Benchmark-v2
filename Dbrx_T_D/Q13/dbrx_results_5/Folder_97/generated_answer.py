def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 81:
        return None
    second_largest = None
    largest = None
    for i in range(40, 81):
        num = numbers[i]
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    if second_largest is not None:
        return second_largest
    else:
        return None