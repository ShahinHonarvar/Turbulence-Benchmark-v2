def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 8:
        return None
    sublist = numbers[:8]
    sublist.sort()
    return sublist[1] if len(sublist) > 1 else None