def find_second_smallest_num(numbers):
    if 55 <= len(numbers) <= 98:
        sublist = sorted(numbers[55:99])
        return sublist[1] if len(sublist) > 1 else None
    return None