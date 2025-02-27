def find_subset_of_length_n(s: set) -> int:
    if len(s) < 87:
        return 0
    else:
        return len(s) * find_subset_of_length_n(s - {s.pop()})