def find_second_smallest_num(numbers):
    if len(numbers) <= 23:
        return None
    sublist = numbers[23:24]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]