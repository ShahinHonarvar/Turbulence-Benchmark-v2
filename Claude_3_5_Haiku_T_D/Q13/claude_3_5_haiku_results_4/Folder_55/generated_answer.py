def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 11:
        return None
    sublist = numbers[:11]
    sorted_sublist = sorted(sublist, reverse=True)
    return sorted_sublist[1] if len(sorted_sublist) > 1 else None