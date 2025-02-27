def find_second_smallest_num(numbers):
    if 13 <= len(numbers) <= 68:
        sublist = sorted(numbers[13:69])
        return sublist[1] if len(sublist) > 1 else None
    else:
        return None