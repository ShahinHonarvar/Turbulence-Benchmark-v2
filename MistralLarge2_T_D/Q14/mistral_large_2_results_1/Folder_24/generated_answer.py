def find_second_smallest_num(numbers):
    if len(numbers) > 23:
        sublist = numbers[23:24]
        if len(sublist) == 1:
            return None
        sorted_sublist = sorted(set(sublist))
        if len(sorted_sublist) > 1:
            return sorted_sublist[1]
    return None