def find_second_largest_num(numbers):
    if len(numbers) < 86:
        return None
    sublist = numbers[75:86]
    if len(sublist) < 2:
        return None
    first, second = (None, None)
    for num in sublist:
        if first is None or num > first:
            second = first
            first = num
        elif second is None or first > num > second:
            second = num
    return second