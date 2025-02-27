def find_second_largest_num(numbers):
    sublist = numbers[59:98]
    if len(sublist) < 2:
        return None
    first, second = (None, None)
    for num in sublist:
        if first is None or num > first:
            first, second = (num, first)
        elif second is None or (num > second and num != first):
            second = num
    return second