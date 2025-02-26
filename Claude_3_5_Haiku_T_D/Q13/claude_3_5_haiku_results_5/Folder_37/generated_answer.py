def find_second_largest_num(numbers):
    if len(numbers) < 6:
        return None
    sublist = numbers[1:6]
    if len(set(sublist)) < 2:
        return None
    sorted_sublist = sorted(sublist, reverse=True)
    return sorted_sublist[1]