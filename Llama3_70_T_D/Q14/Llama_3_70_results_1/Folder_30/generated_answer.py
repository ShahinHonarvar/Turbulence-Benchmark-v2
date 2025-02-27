def find_second_smallest_num(numbers):
    if len(numbers) < 53:
        return None
    sublist = numbers[26:53]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]