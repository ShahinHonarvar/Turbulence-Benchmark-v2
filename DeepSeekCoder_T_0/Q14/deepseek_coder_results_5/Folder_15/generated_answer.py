def find_second_smallest_num(numbers):
    if len(numbers) < 4:
        return None
    sublist = numbers[:4]
    sublist.sort()
    return sublist[1] if len(sublist) > 1 else None