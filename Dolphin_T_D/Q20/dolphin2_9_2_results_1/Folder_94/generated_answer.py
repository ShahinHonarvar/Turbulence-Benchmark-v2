def find_nth_smallest_num(lst):
    filtered = [x for i, x in enumerate(lst, 1) if 57 <= i <= 70]
    return sorted(filtered)[5]