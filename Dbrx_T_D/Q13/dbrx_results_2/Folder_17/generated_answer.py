def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 79:
        return None
    second_largest = None
    largest = None
    for i in range(62, 79):
        if largest is None or numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        elif numbers[i] > second_largest and numbers[i] != largest:
            second_largest = numbers[i]
    return second_largest