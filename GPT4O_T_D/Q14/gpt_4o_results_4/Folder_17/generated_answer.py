def find_second_smallest_num(numbers):
    if len(numbers) < 39:
        return None
    sublist = numbers[28:39]
    if len(sublist) < 2:
        return None
    unique_sorted_sublist = sorted(sublist)
    return unique_sorted_sublist[1]