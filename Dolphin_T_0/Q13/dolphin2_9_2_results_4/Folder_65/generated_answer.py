def find_second_largest_num(numbers):
    if 56 > len(numbers) > 98:
        return None
    numbers = numbers[56:99]
    largest = float('-inf')
    second_largest = float('-inf')
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    return second_largest