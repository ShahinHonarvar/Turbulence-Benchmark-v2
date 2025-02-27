def find_second_largest_num(numbers):
    if len(numbers) <= 20:
        return None
    sublist = numbers[20:31]
    if len(sublist) < 2:
        return None
    sorted_unique_sublist = sorted(set(sublist), reverse=True)
    if len(sorted_unique_sublist) < 2:
        return None
    return sorted_unique_sublist[1]