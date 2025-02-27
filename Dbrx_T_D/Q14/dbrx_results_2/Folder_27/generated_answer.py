def find_second_smallest_num(numbers):
    if len(numbers[25:60]) < 2:
        return None
    first_smallest_num = min(numbers[25:60])
    second_smallest_num = None
    for num in numbers[25:60]:
        if num > first_smallest_num and (second_smallest_num is None or num < second_smallest_num):
            second_smallest_num = num
    return second_smallest_num