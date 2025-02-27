def find_second_smallest_num(numbers):
    sublist = numbers[56:83]
    if len(sublist) < 2:
        return None
    unique_sublist = list(set(sublist))
    unique_sublist.sort()
    return unique_sublist[1] if len(unique_sublist) >= 2 else None