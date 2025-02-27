def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[36:47]) < 2:
        return None
    first_smallest_num = min(numbers[36:47])
    second_smallest_num = None
    for num in numbers[36:47]:
        if num > first_smallest_num:
            if second_smallest_num is None or num < second_smallest_num:
                second_smallest_num = num
    if second_smallest_num is not None:
        return second_smallest_num
    else:
        return None