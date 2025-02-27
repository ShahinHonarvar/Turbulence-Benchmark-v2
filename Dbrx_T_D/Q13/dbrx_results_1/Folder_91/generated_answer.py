def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 6:
        return None
    first_largest = max(numbers[0:6])
    second_largest = float('-inf')
    for num in numbers[0:6]:
        if num > second_largest and num < first_largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    else:
        return second_largest