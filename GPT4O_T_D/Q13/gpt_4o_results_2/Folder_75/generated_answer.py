def find_second_largest_num(numbers):
    sublist = numbers[56:58]
    if len(sublist) < 2:
        return None
    first, second = (sublist[0], None)
    for num in sublist[1:]:
        if num > first:
            second = first
            first = num
        elif second is None or num > second:
            second = num
    return second