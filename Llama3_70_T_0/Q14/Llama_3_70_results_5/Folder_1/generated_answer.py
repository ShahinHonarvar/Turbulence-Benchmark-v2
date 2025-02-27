def find_second_smallest_num(numbers):
    if len(numbers) < 56:
        return None
    sublist = numbers[34:56]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]