def find_second_smallest_num(numbers):
    if len(numbers) < 8:
        return None
    sublist = numbers[:8]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]