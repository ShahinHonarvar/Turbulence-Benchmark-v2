def find_second_smallest_num(numbers):
    if len(numbers) < 96:
        return None
    sublist = numbers[74:96]
    if len(sublist) < 2:
        return None
    return sorted(set(sublist))[1] if len(set(sublist)) >= 2 else None