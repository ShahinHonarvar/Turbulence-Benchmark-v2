def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    largest = second_largest = float('-inf')
    for number in numbers:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest and number != largest:
            second_largest = number
    if second_largest == float('-inf'):
        return None
    return second_largest