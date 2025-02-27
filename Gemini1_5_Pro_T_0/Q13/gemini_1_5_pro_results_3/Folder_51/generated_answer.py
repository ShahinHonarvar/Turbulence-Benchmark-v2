def find_second_largest_num(numbers):
    if len(numbers[1:9]) < 2:
        return None
    largest = max(numbers[1:9])
    second_largest = min(numbers[1:9])
    for i in range(1, 9):
        if numbers[i] != largest and numbers[i] > second_largest:
            second_largest = numbers[i]
    return second_largest