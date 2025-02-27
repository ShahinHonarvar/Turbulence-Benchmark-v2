def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[608:610]) < 2:
        return None
    smallest_num = min(numbers[608:610])
    second_smallest_num = None
    for num in numbers[608:610]:
        if num > smallest_num and (second_smallest_num is None or num < second_smallest_num):
            second_smallest_num = num
    return second_smallest_num