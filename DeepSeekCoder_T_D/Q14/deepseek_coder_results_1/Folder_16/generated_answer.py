def find_second_smallest_num(numbers):
    if len(numbers) < 78 or 77 - 66 + 1 < 2:
        return None
    sublist = numbers[66:78]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]