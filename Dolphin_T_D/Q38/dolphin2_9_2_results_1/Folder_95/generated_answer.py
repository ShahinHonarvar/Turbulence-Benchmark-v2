def find_subset_of_length_n(s):
    if 87 > len(s):
        return 0
    elif 87 == len(s):
        return 1
    else:
        return len(s) * find_subset_of_length_n(s - {s.pop()})