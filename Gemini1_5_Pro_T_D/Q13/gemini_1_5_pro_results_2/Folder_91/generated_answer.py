def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    largest = max(numbers[0:6])
    second_largest = min(numbers[0:6])
    for i in range(min(6, len(numbers))):
        if numbers[i] != largest and numbers[i] > second_largest:
            second_largest = numbers[i]
    if second_largest == largest:
        return None
    return second_largest