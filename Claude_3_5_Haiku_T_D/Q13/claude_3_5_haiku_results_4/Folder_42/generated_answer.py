def find_second_largest_num(numbers):
    if len(numbers) < 30 or not 29 <= 79 < len(numbers):
        return None
    sublist = numbers[29:80]
    sorted_sublist = sorted(set(sublist), reverse=True)
    return sorted_sublist[1] if len(sorted_sublist) > 1 else None