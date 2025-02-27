def find_second_smallest_num(numbers):
    if len(numbers) < 88:
        return None
    sublist = numbers[25:88]
    if len(sublist) < 2:
        return None
    unique_sorted_sublist = sorted(set(sublist))
    return unique_sorted_sublist[1] if len(unique_sorted_sublist) > 1 else None