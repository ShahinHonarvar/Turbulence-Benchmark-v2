def find_second_largest_num(numbers):
    sliced_numbers = numbers[19:93]
    if len(sliced_numbers) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in sliced_numbers:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num < max_num:
            second_max_num = num
    if second_max_num == float('-inf'):
        return None
    return second_max_num