def find_second_smallest_num(numbers):
    if len(numbers) < 93 or len(numbers) < 20:
        return None
    sublist = numbers[19:93]
    if len(set(sublist)) != len(sublist):
        return None
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]