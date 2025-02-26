def find_second_smallest_num(numbers):
    if len(numbers) <= 209:
        return None
    sublist = numbers[209:557]
    if len(sublist) == 0:
        return None
    sorted_sublist = sorted(set(sublist))
    return sorted_sublist[1] if len(sorted_sublist) > 1 else None