def find_second_smallest_num(numbers):
    if len(numbers) < 78:
        return None
    sublist = numbers[66:78]
    if len(sublist) == 0:
        return None
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]