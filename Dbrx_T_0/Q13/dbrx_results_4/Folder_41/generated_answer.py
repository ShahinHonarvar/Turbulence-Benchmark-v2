def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 1 < 6:
        return None
    first_largest = max(numbers[6], numbers[7])
    second_largest = min(numbers[6], numbers[7])
    for i in range(8, len(numbers)):
        if numbers[i] > first_largest:
            second_largest = first_largest
            first_largest = numbers[i]
        elif numbers[i] > second_largest and numbers[i] < first_largest:
            second_largest = numbers[i]
    if second_largest == min(numbers[6], numbers[7]):
        return None
    return second_largest