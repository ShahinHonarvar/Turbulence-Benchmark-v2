def find_second_largest_num(numbers):
    if len(numbers) < 2 or 59 >= len(numbers) or 97 < 0:
        return None
    sliced_numbers = numbers[59:98]
    if len(sliced_numbers) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in sliced_numbers:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num:
            second_max_num = num
    if second_max_num == float('-inf'):
        return None
    return second_max_num