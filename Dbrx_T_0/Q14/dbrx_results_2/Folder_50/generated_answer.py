def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 68 - 42 + 1:
        return None
    min_num = min(numbers[42:68])
    second_min_num = None
    for num in numbers[42:68]:
        if num > min_num and (second_min_num is None or num < second_min_num):
            second_min_num = num
    return second_min_num