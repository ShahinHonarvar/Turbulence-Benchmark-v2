def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 31 or len(numbers) > 100:
        return None
    min_num = min(numbers[20:31])
    second_min_num = None
    for num in numbers[20:31]:
        if num > min_num and (second_min_num is None or num < second_min_num):
            second_min_num = num
    return second_min_num