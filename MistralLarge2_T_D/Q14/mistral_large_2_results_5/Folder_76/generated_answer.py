def find_second_smallest_num(numbers):
    if len(numbers) < 606:
        return None
    sublist = sorted(numbers[533:606])
    return sublist[1] if len(sublist) > 1 else None