def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num, second_min_num = (min(numbers[0], numbers[1]), max(numbers[0], numbers[1]))
    for num in numbers[2:]:
        if num < min_num:
            second_min_num = min_num
            min_num = num
        elif num < second_min_num and num > min_num:
            second_min_num = num
    return second_min_num if len(numbers) > 1 else None