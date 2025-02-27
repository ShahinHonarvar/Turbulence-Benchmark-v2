def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first, second = (None, None)
    for num in numbers[:10]:
        if first is None or num > first:
            first, second = (num, first)
        elif num > second and num < first:
            second = num
    return second