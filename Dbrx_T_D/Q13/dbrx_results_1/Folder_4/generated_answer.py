def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first_largest, second_largest = (None, None)
    for i in range(12, 93):
        if numbers[i] > first_largest:
            second_largest = first_largest
            first_largest = numbers[i]
        elif numbers[i] > second_largest and numbers[i] < first_largest:
            second_largest = numbers[i]
    return second_largest