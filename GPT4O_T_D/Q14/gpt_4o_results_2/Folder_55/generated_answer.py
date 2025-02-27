def find_second_smallest_num(numbers):
    if len(numbers) <= 10:
        return None
    sublist = numbers[10:11]
    if len(sublist) <= 1:
        return None
    sorted_unique_sublist = sorted(set(sublist))
    if len(sorted_unique_sublist) < 2:
        return None
    return sorted_unique_sublist[1]