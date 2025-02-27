def find_second_smallest_num(numbers):
    if 15 <= len(numbers) <= 39:
        sublist = sorted(numbers[15:40])
        return sublist[1] if len(sublist) > 1 else None
    return None