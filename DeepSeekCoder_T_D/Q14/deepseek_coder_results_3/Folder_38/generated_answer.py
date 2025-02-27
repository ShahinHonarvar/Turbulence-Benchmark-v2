def find_second_smallest_num(numbers):
    if len(numbers) < 52 or len(numbers) < 38:
        return None
    sublist = numbers[37:52]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]