def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 28 or len(numbers) > 38:
        return None
    smallest_num = min(numbers[28:39])
    second_smallest_num = None
    for num in numbers[28:39]:
        if num > smallest_num and (second_smallest_num is None or num < second_smallest_num):
            second_smallest_num = num
    return second_smallest_num if second_smallest_num is not None else None