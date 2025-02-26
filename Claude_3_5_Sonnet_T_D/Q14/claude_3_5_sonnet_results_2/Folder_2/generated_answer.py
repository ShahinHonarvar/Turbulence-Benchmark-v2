def find_second_smallest_num(numbers):
    if len(numbers) < 87 or len(numbers[43:87]) < 2:
        return None
    sublist = numbers[43:87]
    sorted_sublist = sorted(set(sublist))
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]