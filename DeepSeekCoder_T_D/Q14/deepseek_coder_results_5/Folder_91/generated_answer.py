def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 6:
        return None
    sublist = numbers[:6]
    sublist.sort()
    return sublist[1] if len(sublist) > 1 else None