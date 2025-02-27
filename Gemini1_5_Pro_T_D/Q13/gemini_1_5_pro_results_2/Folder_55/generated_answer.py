def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 11:
        return None
    largest = max(numbers[0:11])
    second_largest = min(numbers[0:11])
    for i in range(0, 11):
        if numbers[i] != largest and numbers[i] > second_largest:
            second_largest = numbers[i]
    if second_largest == largest:
        return None
    return second_largest