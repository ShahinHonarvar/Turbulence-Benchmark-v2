def find_second_smallest_num(numbers):
    if len(numbers) < 89:
        return None
    sublist = numbers[75:89]
    if len(sublist) < 2:
        return None
    sublist_sorted = sorted(sublist)
    return sublist_sorted[1]