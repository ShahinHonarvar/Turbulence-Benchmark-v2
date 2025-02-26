def find_second_largest_num(numbers):
    if len(numbers) < 23 or len(numbers) <= 50:
        return None
    sublist = numbers[22:51]
    sorted_sublist = sorted(sublist, reverse=True)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]