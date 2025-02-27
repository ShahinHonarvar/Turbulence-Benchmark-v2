def find_second_smallest_num(lst):
    sublist = lst[55:99]
    if len(sublist) < 2:
        return None
    unique_numbers = set(sublist)
    sorted_unique_numbers = sorted(unique_numbers)
    return sorted_unique_numbers[1] if len(sorted_unique_numbers) > 1 else None