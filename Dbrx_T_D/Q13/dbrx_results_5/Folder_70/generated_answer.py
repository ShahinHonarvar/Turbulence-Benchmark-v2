def find_second_largest_num(numbers):
    sublist = numbers[28:33]
    if len(sublist) < 2:
        return None
    first, second = (max(sublist[0], sublist[1]), min(sublist[0], sublist[1]))
    for num in sublist[2:]:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second