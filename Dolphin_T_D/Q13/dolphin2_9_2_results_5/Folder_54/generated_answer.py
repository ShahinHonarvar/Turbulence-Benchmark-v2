def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    second_largest = None
    largest = float('-inf')
    for i in range(34, 55):
        if numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        elif second_largest < numbers[i] < largest:
            second_largest = numbers[i]
    return second_largest