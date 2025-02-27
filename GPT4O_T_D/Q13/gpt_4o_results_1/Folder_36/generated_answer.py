def find_second_largest_num(numbers):
    if len(numbers) < 751:
        return None
    sublist = numbers[246:751]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist, reverse=True)
    return sorted_sublist[1]