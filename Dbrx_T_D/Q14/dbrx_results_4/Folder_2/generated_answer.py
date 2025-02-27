def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 43 or len(numbers) < 86:
        return None
    min_num = min(numbers[42:87])
    second_min_num = None
    for num in numbers[42:87]:
        if num > min_num:
            if second_min_num is None or num < second_min_num:
                second_min_num = num
    return second_min_num