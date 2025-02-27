def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers[:11]) < 2:
        return None
    largest = max(numbers[:11])
    second_largest = min(numbers[:11])
    for i in range(min(11, len(numbers))):
        if numbers[i] != largest and numbers[i] > second_largest:
            second_largest = numbers[i]
    return second_largest