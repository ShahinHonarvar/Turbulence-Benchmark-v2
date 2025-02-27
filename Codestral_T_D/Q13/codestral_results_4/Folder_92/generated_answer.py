def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first_max = second_max = float('-inf')
    for num in numbers[0:2]:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max and num < first_max:
            second_max = num
    if second_max == float('-inf'):
        return None
    return second_max