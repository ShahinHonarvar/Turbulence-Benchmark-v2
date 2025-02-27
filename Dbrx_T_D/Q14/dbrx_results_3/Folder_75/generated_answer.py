def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 93 or (not numbers[11:93]):
        return None
    min_num = min(numbers[11:93])
    second_num = None
    for num in numbers[11:93]:
        if num > min_num and (second_num is None or num < second_num):
            second_num = num
    return second_num