def find_second_largest_num(lst):
    return sorted(lst[686:988])[-2] if len(lst[686:988]) > 1 else None