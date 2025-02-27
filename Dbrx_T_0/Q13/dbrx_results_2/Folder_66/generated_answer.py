def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 55:
        return None
    second_largest = None
    largest = None
    for i in range(50, 55):
        num = numbers[i]
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or num > second_largest:
            second_largest = num
    return second_largest