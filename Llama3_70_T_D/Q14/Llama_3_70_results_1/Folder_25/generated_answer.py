def find_second_smallest_num(numbers):
    if len(numbers) < 77:
        return None
    sublist = numbers[37:77]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]