def find_second_largest_num(numbers):
    if len(numbers) <= 23:
        return None
    sublist = numbers[23:24]
    if len(sublist) == 0:
        return None
    return sorted(set(sublist), reverse=True)[1] if len(set(sublist)) > 1 else None