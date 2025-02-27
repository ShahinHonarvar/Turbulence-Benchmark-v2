def find_second_largest_num(numbers):
    if len(numbers) < 65:
        return None
    sliced_numbers = numbers[14:65]
    if len(sliced_numbers) < 2:
        return None
    max_num = second_max = float('-inf')
    for num in sliced_numbers:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num < max_num:
            second_max = num
    return second_max if second_max != float('-inf') else None