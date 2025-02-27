def find_second_smallest_num(numbers):
    if len(numbers) < 93:
        return None
    sublist = numbers[62:93]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]