def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 100 or (not isinstance(numbers, list)):
        return None
    first_half = numbers[62:100]
    second_largest = None
    largest = None
    for num in first_half:
        if not isinstance(num, (int, float)):
            continue
        if largest is None or num > largest:
            largest, second_largest = (num, largest)
        elif second_largest is None or num > second_largest:
            second_largest = num
    if second_largest is not None and second_largest < largest:
        return second_largest
    else:
        return None