def find_second_largest_num(numbers):
    if len(numbers) < 35:
        return None
    second_largest = float('-inf')
    largest = float('-inf')
    for num in numbers[31:35]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num < largest and num > second_largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    return second_largest