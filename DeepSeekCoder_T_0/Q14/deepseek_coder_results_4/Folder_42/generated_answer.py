def find_second_smallest_num(numbers):
    if len(numbers) < 98:
        return None
    sublist = numbers[21:98]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]