def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 26 or len(numbers) > 52:
        return None
    first_smallest_num = min(numbers[26:53])
    second_smallest_num = None
    for num in numbers[26:53]:
        if num > first_smallest_num and (second_smallest_num is None or num < second_smallest_num):
            second_smallest_num = num
    return second_smallest_num