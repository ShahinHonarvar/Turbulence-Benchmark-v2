def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 8:
        return None
    largest = numbers[1]
    second_largest = None
    for i in range(1, min(len(numbers), 9)):
        if numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        elif numbers[i] != largest and (second_largest is None or numbers[i] > second_largest):
            second_largest = numbers[i]
    return second_largest