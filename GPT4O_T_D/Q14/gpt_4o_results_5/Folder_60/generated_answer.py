def find_second_smallest_num(lst):
    sublist = lst[56:99]
    if len(sublist) < 2:
        return None
    unique_numbers = sorted(set(sublist))
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]