def find_second_largest_num(numbers):
    sublist = numbers[4:5]
    if len(sublist) < 2:
        return None
    first, second = (sublist[0], None) if sublist[0] >= sublist[1] else (sublist[1], sublist[0])
    for num in sublist[2:]:
        if num > first:
            second = first
            first = num
        elif second is None or num > second:
            second = num
    return second