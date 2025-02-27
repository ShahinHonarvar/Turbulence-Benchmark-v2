def find_second_smallest_num(numbers):
    if len(numbers) < 87 or len(numbers) < 44:
        return None
    sublist = numbers[43:87]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]