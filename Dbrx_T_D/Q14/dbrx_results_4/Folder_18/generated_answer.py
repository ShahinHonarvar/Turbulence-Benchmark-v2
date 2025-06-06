def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 49 or len(numbers) > 100:
        return None
    min_num = min(numbers[30:49])
    second_min_num = None
    for num in numbers[30:49]:
        if num > min_num and (second_min_num is None or num < second_min_num):
            second_min_num = num
    if second_min_num is None:
        return None
    else:
        return second_min_num