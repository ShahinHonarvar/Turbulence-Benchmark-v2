def find_second_smallest_num(numbers):
    if len(numbers) < 98:
        return None
    numbers = numbers[55:99]
    smallest_num = min(numbers)
    second_smallest_num = None
    for num in numbers:
        if num > smallest_num and (num < second_smallest_num or second_smallest_num is None):
            second_smallest_num = num
    return second_smallest_num