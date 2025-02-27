def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 925 or len(numbers) > 1000:
        return None
    second_largest = None
    largest = max(numbers[:264])
    for num in numbers[264:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or num > second_largest:
            if num != largest:
                second_largest = num
    return second_largest