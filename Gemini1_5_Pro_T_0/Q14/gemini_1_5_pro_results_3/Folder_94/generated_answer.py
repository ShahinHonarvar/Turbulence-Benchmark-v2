def find_second_smallest_num(numbers):
    if len(numbers) < 72:
        return None
    sublist = numbers[52:72]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]