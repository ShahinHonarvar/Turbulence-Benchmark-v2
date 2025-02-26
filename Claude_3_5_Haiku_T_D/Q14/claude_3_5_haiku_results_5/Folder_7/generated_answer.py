def find_second_smallest_num(numbers):
    if len(numbers) <= 687:
        return None
    sublist = numbers[686:988]
    if len(sublist) < 2:
        return None
    unique_sublist = sorted(set(sublist))
    return unique_sublist[1] if len(unique_sublist) >= 2 else None