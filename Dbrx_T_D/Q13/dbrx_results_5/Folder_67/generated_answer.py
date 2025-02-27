def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 50 or len(numbers) < 22:
        return None
    max_num = max(numbers[22:51])
    second_max_num = None
    for num in numbers[22:51]:
        if num < max_num and (second_max_num is None or num > second_max_num):
            second_max_num = num
    return second_max_num