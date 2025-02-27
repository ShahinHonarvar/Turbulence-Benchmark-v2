def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    sublist = numbers[5:8]
    if len(sublist) < 2:
        return None
    first, second = (None, None)
    for num in sublist:
        if first is None or num < first:
            second, first = (first, num)
        elif num < first:
            second = num
    if second is not None:
        return second
    else:
        return None