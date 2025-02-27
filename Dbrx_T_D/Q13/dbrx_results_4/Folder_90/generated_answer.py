def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 262 or len(numbers) > 746:
        return None
    first, second = (max(numbers[262:746], default=None), None)
    for num in numbers[262:746]:
        if num > first:
            first, second = (num, first)
        elif first is not None and num > second and (num < first):
            second = num
    return second