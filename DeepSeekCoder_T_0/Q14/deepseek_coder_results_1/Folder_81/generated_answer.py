def find_second_smallest_num(numbers):
    if len(numbers) < 101:
        return None
    sublist = numbers[10:101]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]