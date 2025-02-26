def find_second_smallest_num(numbers):
    if len(numbers) < 37:
        return None
    sublist = numbers[33:37]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) >= 2:
        return sorted_sublist[1]
    else:
        return None