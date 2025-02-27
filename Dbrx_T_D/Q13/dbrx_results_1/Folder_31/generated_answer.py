def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 14:
        return None
    second_largest_num = None
    largest_num = max(numbers[75:89])
    for num in numbers[75:89]:
        if num < largest_num and (second_largest_num is None or num > second_largest_num):
            second_largest_num = num
    return second_largest_num