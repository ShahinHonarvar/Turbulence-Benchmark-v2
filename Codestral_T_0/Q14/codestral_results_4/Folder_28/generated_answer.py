def find_second_smallest_num(numbers):
    if 22 <= len(numbers) <= 50:
        sublist = sorted(numbers[22:51])
        return sublist[1] if len(sublist) > 1 else None
    return None