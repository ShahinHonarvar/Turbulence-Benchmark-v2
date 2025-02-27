def find_second_smallest_num(numbers):
    if 4 < len(numbers) - 1:
        sublist = sorted(numbers[4:5])
        return sublist[1] if len(sublist) > 1 else None
    return None