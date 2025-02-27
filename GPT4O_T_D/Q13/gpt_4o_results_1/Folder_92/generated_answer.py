def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    sublist = numbers[:2]
    return min(sublist) if len(sublist) == 2 else None