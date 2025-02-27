def find_second_smallest_num(numbers):
    if len(numbers) <= 10:
        return None
    sublist = numbers[10:11]
    if len(sublist) < 2:
        return None
    sublist_sorted = sorted(sublist)
    return sublist_sorted[1]