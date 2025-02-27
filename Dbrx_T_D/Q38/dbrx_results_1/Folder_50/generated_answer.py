def find_subset_of_length_n(s: set) -> int:
    if len(s) < 40:
        return 0
    elif len(s) == 40:
        return 1
    else:
        return sum((find_subset_of_length_n(s.difference({e})) for e in s))