def find_second_smallest_num(numbers):
    if len(numbers) < 747 or len(numbers) < 262:
        return None
    sublist = numbers[262:747]
    if len(set(sublist)) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]