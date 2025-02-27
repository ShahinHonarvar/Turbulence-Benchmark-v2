def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    sublist = numbers[:7]
    unique_sorted = sorted(sublist)
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[1]