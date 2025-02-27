def find_subset_of_length_n(s):
    if len(s) < 801:
        return 0
    elif len(s) == 801:
        return 1
    else:
        return find_subset_of_length_n(s - {s.pop()}) + find_subset_of_length_n(s)