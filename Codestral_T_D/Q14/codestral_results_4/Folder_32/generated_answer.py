def find_second_smallest_num(numbers):
    if 32 <= len(numbers) <= 35:
        sublist = sorted(numbers[32:36])
        return sublist[1] if len(sublist) > 1 else None
    else:
        return None