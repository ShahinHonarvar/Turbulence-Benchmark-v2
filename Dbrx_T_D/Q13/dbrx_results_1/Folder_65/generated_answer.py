def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 43:
        return None
    second_largest = None
    largest = None
    for i in range(56, 99):
        num = numbers[i]
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or (num > second_largest and num < largest):
            second_largest = num
    return second_largest