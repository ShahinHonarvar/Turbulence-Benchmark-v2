def find_second_smallest_num(numbers):
    if len(numbers) < 51 or len(numbers) < 23:
        return None
    sublist = numbers[22:51]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]