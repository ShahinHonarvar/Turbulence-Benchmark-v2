def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 10:
        return None
    largest = max(numbers[0:10])
    second_largest = min(numbers[0:10])
    for i in range(min(10, len(numbers))):
        if numbers[i] != largest and numbers[i] > second_largest:
            second_largest = numbers[i]
    return second_largest