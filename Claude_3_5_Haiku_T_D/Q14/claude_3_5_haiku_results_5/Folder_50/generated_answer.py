def find_second_smallest_num(numbers):
    if len(numbers) < 43:
        return None
    sublist = numbers[42:69]
    if len(sublist) == 0:
        return None
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]