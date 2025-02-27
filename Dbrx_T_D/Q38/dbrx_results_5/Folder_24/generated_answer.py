def find_subset_of_length_n(elements):
    if len(elements) < 74:
        return 0
    if len(elements) == 74:
        return 1 if sum(elements) == 0 else 0
    return sum((find_subset_of_length_n(elements[:i]) for i in range(1, len(elements))))