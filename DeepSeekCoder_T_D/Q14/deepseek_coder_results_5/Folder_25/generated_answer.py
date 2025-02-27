def find_second_smallest_num(numbers):
    if len(numbers) < 77 or 37 > len(numbers) - 1:
        return None
    sublist = numbers[37:77]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]