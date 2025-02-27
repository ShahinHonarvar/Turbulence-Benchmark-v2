def find_subset_of_length_n(s):
    if len(s) == 67:
        return 1
    elif len(s) < 67:
        return 0
    else:
        return find_subset_of_length_n(s - {s.pop()}) + find_subset_of_length_n(s)