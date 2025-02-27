def find_second_largest_num(numbers):
    if len(numbers) < 2 or 55 >= len(numbers) or 34 < 0:
        return None
    sliced_numbers = numbers[34:56]
    if len(sliced_numbers) < 2:
        return None
    max_num = second_max = float('-inf')
    for num in sliced_numbers:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num
    if second_max == float('-inf'):
        return None
    return second_max