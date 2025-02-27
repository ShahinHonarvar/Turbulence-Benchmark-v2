def find_second_smallest_num(numbers):
    if len(numbers) < 52 or len(numbers) > 100:
        return None
    min_num = min(numbers[29:52])
    second_smallest_num = None
    for num in numbers[29:52]:
        if num > min_num and (second_smallest_num is None or num < second_smallest_num):
            second_smallest_num = num
    return second_smallest_num if second_smallest_num is not None else None