def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 55 or len(numbers) < 98:
        return None
    first, second = (None, None)
    for num in numbers[55:99]:
        if first is None or num > first:
            first, second = (num, first)
        elif num > second and num < first:
            second = num
    if second is not None:
        return second
    else:
        return None