def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 88:
        return None
    min_num = min(numbers[30:88])
    second_min_num = None
    for num in numbers[30:88]:
        if num > min_num and (num < second_min_num or second_min_num is None):
            second_min_num = num
    return second_min_num