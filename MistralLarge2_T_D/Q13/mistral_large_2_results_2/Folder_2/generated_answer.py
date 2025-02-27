def find_second_largest_num(numbers):
    if len(numbers) < 40:
        return None
    sublist = numbers[15:40]
    if len(sublist) < 2:
        return None
    sublist = sorted(sublist, reverse=True)
    return sublist[1] if len(sublist) > 1 else None