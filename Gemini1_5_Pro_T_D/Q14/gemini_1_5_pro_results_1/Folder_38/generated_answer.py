def find_second_smallest_num(numbers):
    if len(numbers) < 52:
        return None
    sublist = numbers[37:52]
    if len(set(sublist)) != len(sublist):
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]