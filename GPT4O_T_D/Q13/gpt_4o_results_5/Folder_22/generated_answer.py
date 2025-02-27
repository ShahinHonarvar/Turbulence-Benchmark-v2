def find_second_largest_num(numbers):
    if len(numbers) < 201:
        return None
    sublist = numbers[40:201]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(set(sublist), reverse=True)
    return sorted_sublist[1] if len(sorted_sublist) > 1 else None