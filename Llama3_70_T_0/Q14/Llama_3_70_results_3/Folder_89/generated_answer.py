def find_second_smallest_num(numbers):
    if len(numbers) < 64:
        return None
    sublist = numbers[62:64]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]