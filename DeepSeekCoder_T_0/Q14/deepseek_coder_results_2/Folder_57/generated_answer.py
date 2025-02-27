def find_second_smallest_num(numbers):
    if len(numbers) < 31:
        return None
    sublist = numbers[20:31]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]