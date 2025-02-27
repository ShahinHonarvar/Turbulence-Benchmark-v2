def find_second_largest_num(numbers):
    if len(numbers) < 8:
        return None
    largest = max(numbers[0:8])
    second_largest = min(numbers[0:8])
    for i in range(8):
        if numbers[i] != largest and numbers[i] > second_largest:
            second_largest = numbers[i]
    if second_largest == largest:
        return None
    return second_largest