def find_second_smallest_num(numbers):
    sublist = numbers[19:93]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(set(sublist))
    return sorted_sublist[1] if len(sorted_sublist) > 1 else None