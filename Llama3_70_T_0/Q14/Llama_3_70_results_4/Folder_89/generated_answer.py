def find_second_smallest_num(numbers):
    if len(numbers) < 64:
        return None
    sublist = numbers[62:64]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]