def find_second_largest_num(numbers):
    if len(numbers) < 98:
        return None
    sublist = numbers[59:98]
    if len(sublist) < 2:
        return None
    sublist_sorted = sorted(sublist, reverse=True)
    return sublist_sorted[1]