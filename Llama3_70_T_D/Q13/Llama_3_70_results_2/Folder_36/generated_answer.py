def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    sliced_numbers = numbers[246:751]
    if not sliced_numbers:
        return None
    largest = second_largest = float('-inf')
    for num in sliced_numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    return second_largest