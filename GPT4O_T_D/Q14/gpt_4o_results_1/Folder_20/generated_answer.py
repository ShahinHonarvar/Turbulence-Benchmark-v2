def find_second_smallest_num(numbers):
    if len(numbers) < 95:
        return None
    sublist = numbers[75:95]
    if len(sublist) < 2:
        return None
    unique_sorted_sublist = sorted(sublist)
    return unique_sorted_sublist[1]