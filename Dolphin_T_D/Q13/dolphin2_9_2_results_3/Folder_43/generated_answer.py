def find_second_largest_num(numbers):
    sublist = numbers[68:87]
    if len(sublist) < 2:
        return None
    max1 = max(sublist)
    sublist.remove(max1)
    if len(sublist) < 2:
        return None
    max2 = max(sublist)
    return max2