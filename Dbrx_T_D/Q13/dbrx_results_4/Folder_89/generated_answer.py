def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    largest = float('-inf')
    second_largest = float('-inf')
    for num in numbers[56:83]:
        if num > largest:
            second_largest = largest
            largest = num
    if second_largest == float('-inf'):
        return None
    return second_largest