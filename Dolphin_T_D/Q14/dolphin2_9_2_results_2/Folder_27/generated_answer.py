def find_second_smallest_num(numbers):
    sublist = numbers[24:59]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]