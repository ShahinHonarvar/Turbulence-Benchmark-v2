def find_second_smallest_num(numbers):
    if len(numbers) < 4:
        return None
    sublist = numbers[:4]
    sublist.sort()
    if len(sublist) >= 2:
        return sublist[1]
    else:
        return None