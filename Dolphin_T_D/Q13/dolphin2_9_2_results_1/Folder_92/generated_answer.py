def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    max_num = max(numbers[0], numbers[1])
    second_max_num = min(numbers[0], numbers[1])
    for num in numbers[2:]:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num < max_num:
            second_max_num = num
    return second_max_num if second_max_num != numbers[0] else None