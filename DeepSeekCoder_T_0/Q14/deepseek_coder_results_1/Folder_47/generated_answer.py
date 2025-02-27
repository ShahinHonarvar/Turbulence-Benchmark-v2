def find_second_smallest_num(numbers):
    if len(numbers) < 64 or len(numbers) < 23:
        return None
    sublist = numbers[22:64]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]