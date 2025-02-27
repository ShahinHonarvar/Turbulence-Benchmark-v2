def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 85:
        return None
    second_largest = None
    largest = None
    for i in range(70, 85):
        if largest is None or largest < numbers[i]:
            second_largest = largest
            largest = numbers[i]
        elif second_largest is None or second_largest < numbers[i]:
            second_largest = numbers[i]
    if second_largest is not None and second_largest < largest:
        return second_largest
    return None