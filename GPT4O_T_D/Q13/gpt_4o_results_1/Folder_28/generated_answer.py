def find_second_largest_num(numbers):
    if len(numbers) < 64:
        return None
    sublist = sorted(numbers[62:64])
    return sublist[0] if len(sublist) == 2 else None