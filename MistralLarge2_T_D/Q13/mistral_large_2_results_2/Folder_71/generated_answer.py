def find_second_largest_num(numbers):
    if len(numbers) <= 52:
        return None
    sublist = numbers[26:53]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist, reverse=True)
    return sorted_sublist[1]