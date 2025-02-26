def find_second_smallest_num(numbers):
    if len(numbers) < 64:
        return None
    sublist = numbers[22:64]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(set(sublist))
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]