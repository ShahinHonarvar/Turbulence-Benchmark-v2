def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 6:
        return None
    min_num = min(numbers[:5])
    second_num = None
    for num in numbers[:5]:
        if num > min_num and (second_num is None or num < second_num):
            second_num = num
    return second_num