def find_second_smallest_num(numbers):
    if len(numbers) < 83 or 56 > len(numbers):
        return None
    sublist = numbers[56:83]
    if len(set(sublist)) < 2:
        return None
    ordered = sorted(sublist)
    return ordered[1]