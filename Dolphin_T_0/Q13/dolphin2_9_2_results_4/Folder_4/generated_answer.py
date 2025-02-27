def find_second_largest_num(numbers):
    sublist = numbers[12:93]
    if len(sublist) < 2:
        return None
    first = max(sublist)
    sublist.remove(first)
    if len(sublist) < 2:
        return None
    second = max(sublist)
    return second