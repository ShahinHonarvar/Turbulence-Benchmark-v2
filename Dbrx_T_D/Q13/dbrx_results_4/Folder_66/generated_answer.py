def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 55:
        return None
    second_largest = None
    largest = float('-inf')
    for i in range(50, 55):
        if numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        elif numbers[i] > second_largest and numbers[i] < largest:
            second_largest = numbers[i]
    return second_largest