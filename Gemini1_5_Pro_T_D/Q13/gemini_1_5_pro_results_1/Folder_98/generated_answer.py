def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 7:
        return None
    largest = numbers[0]
    second_largest = None
    for i in range(1, 7):
        if i >= len(numbers):
            break
        if numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        elif second_largest is None and numbers[i] != largest:
            second_largest = numbers[i]
        elif second_largest is not None and numbers[i] > second_largest and (numbers[i] != largest):
            second_largest = numbers[i]
    return second_largest