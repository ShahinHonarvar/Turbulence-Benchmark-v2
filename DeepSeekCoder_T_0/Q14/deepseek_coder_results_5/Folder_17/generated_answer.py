def find_second_smallest_num(numbers):
    if len(numbers) < 39:
        return None
    sublist = numbers[28:39]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]