def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 39 - 15 + 1:
        return None
    max_num = max(numbers[15:40])
    second_max_num = None
    for num in numbers[15:40]:
        if num < max_num and (second_max_num is None or num > second_max_num):
            second_max_num = num
    return second_max_num