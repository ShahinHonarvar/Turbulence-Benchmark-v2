def find_second_smallest_num(numbers):
    if len(numbers) < 639 or len(numbers) < 975:
        return None
    sublist = numbers[639:976]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(set(sublist))
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]