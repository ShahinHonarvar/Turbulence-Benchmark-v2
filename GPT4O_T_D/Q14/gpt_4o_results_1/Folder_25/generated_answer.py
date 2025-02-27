def find_second_smallest_num(numbers):
    if len(numbers) < 77:
        return None
    sublist = numbers[37:77]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]