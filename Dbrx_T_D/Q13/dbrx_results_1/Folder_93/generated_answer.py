def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 95:
        return None
    second_largest = None
    largest = None
    for i in range(75, 95):
        if largest is None or numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        elif second_largest is None or numbers[i] > second_largest:
            second_largest = numbers[i]
    if second_largest is not None and largest is not None and (second_largest != largest):
        return second_largest
    else:
        return None