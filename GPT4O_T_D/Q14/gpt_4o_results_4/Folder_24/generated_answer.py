def find_second_smallest_num(numbers):
    if len(numbers) < 24:
        return None
    sublist = numbers[23:24]
    if len(sublist) < 2:
        return None
    unique_sorted_sublist = sorted(set(sublist))
    if len(unique_sorted_sublist) < 2:
        return None
    return unique_sorted_sublist[1]