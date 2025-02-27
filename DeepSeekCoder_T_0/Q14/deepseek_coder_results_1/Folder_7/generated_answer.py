def find_second_smallest_num(numbers):
    if len(numbers) < 988 or len(numbers) < 687:
        return None
    sublist = numbers[686:988]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1] if len(sorted_sublist) > 1 else None