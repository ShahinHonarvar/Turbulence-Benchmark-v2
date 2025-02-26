def find_second_largest_num(numbers):
    if len(numbers) <= 1 or len(numbers) < 10:
        return None
    sublist = numbers[:10]
    sorted_sublist = sorted(set(sublist), reverse=True)
    return sorted_sublist[1] if len(sorted_sublist) >= 2 else None