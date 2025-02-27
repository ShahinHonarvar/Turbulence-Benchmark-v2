def find_second_smallest_num(numbers):
    if len(numbers) < 56:
        return None
    min_num = min((num for num in numbers[13:68]))
    second_min_num = None
    for num in numbers[13:68]:
        if num > min_num and (second_min_num is None or num < second_min_num):
            second_min_num = num
    return second_min_num