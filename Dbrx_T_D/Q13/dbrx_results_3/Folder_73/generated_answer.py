def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 93 - 19 + 1:
        return None
    segment = numbers[19:93]
    first, second = (None, None)
    for num in segment:
        if first is None or num > first:
            second = first
            first = num
        elif second is None or num > second:
            second = num
    return second