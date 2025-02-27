def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 55:
        return None
    numbers = numbers[49:55]
    max_num = max(numbers[0], numbers[1])
    second_max_num = min(max_num, numbers[0]) if max_num != numbers[0] else None
    for num in numbers[2:]:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num < max_num:
            second_max_num = num
    if second_max_num is None:
        return None
    else:
        return second_max_num