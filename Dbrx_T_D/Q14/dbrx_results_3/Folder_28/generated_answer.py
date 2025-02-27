def find_second_smallest_num(numbers):
    if len(numbers) < 50 or len(numbers) > 100 or len(numbers) < 22:
        return None
    min_num = min(numbers[22:51])
    second_min_num = None
    for num in numbers[22:51]:
        if num > min_num and (second_min_num is None or num < second_min_num):
            second_min_num = num
    return second_min_num