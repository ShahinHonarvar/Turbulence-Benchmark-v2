def find_second_largest_num(numbers):
    if len(numbers) < 3 or len(numbers) < 67:
        return None
    second_largest = None
    largest = max(numbers[64:67])
    for num in numbers[64:66]:
        if num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or num > second_largest:
            second_largest = num
    if second_largest is not None and second_largest < largest:
        return second_largest
    else:
        return None