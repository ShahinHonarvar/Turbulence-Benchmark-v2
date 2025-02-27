def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    largest = float('-inf')
    second_largest = float('-inf')
    for i in range(5, 8):
        if numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        elif numbers[i] > second_largest and numbers[i] != largest:
            second_largest = numbers[i]
    if second_largest == float('-inf'):
        return None
    return second_largest