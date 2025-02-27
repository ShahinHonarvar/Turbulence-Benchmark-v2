def find_second_smallest_num(numbers):
    if len(numbers) < 47:
        return None
    sublist = numbers[36:47]
    if len(sublist) < 2:
        return None
    unique_sublist = list(set(sublist))
    unique_sublist.sort()
    return unique_sublist[1] if len(unique_sublist) > 1 else None