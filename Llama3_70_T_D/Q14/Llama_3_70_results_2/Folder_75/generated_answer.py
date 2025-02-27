def find_second_smallest_num(numbers):
    if len(numbers) < 93:
        return None
    sublist = numbers[12:93]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]