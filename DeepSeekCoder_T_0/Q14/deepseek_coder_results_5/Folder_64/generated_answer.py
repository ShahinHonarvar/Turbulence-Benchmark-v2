def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    sublist = sorted(numbers[:5])
    return sublist[1] if len(sublist) > 1 else None