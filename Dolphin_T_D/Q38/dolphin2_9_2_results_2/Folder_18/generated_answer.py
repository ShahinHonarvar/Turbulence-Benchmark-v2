def find_subset_of_length_n(s):
    if not s:
        return 0
    if len(s) == 630:
        return 1
    return len(s) * find_subset_of_length_n(s - {s.pop()})