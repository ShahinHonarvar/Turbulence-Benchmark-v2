def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 9:
        return None
    largest = numbers[0]
    second_largest = None
    for i in range(1, 9):
        if i >= len(numbers):
            break
        if numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        elif second_largest is None or numbers[i] > second_largest:
            second_largest = numbers[i]
    return second_largest