def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 100 or len(numbers) > 10000:
        return None
    first_largest = None
    second_largest = None
    for i in range(91, 100):
        if first_largest is None or numbers[i] > first_largest:
            second_largest = first_largest
            first_largest = numbers[i]
        elif second_largest is None or numbers[i] > second_largest:
            second_largest = numbers[i]
    if second_largest is None:
        return None
    else:
        return second_largest