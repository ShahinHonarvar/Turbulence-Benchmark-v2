def find_second_smallest_num(numbers):
    if 72 < len(numbers) < 31:
        return None
    sublist = numbers[31:73]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]