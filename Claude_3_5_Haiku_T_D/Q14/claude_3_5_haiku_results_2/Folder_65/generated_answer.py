def find_second_smallest_num(numbers):
    if len(numbers) < 58:
        return None
    sublist = numbers[56:58]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]