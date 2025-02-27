def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    second_largest = None
    largest = None
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or second_largest < num < largest:
            second_largest = num
    return second_largest