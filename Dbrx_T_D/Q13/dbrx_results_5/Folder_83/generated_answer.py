def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first, second = (None, None)
    for i in range(90, 91):
        if i >= len(numbers) or numbers[i] in (first, second):
            continue
        if first is None or numbers[i] > first:
            second, first = (first, numbers[i])
        elif second is None or numbers[i] > second:
            second = numbers[i]
    return second