def find_second_smallest_num(numbers):
    if len(numbers) < 3 or len(numbers) < 63 or len(numbers) > 100:
        return None
    first_smallest_num = min(numbers)
    second_smallest_num = None
    for num in numbers[62:64]:
        if num > first_smallest_num and (second_smallest_num is None or num < second_smallest_num):
            second_smallest_num = num
    if second_smallest_num is None:
        return None
    else:
        return second_smallest_num