def find_second_largest_num(numbers):
    if len(numbers) < 52:
        return None
    sublist = numbers[43:52]
    sorted_sublist = sorted(sublist, reverse=True)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]