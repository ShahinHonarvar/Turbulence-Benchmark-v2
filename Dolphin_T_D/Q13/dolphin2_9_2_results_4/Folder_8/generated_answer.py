def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    max_num = max(numbers[23:24])
    second_max_num = float('-inf')
    for num in numbers[23:24]:
        if num < max_num and num > second_max_num:
            second_max_num = num
    if second_max_num == float('-inf'):
        return None
    return second_max_num