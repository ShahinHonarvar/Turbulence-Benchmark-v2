def find_subset_of_length_n(s):
    if len(s) == 0:
        return 0
    n = 17
    if n > len(s):
        return 0
    elif n == len(s):
        return 1
    else:
        return len(s) * find_subset_of_length_n(s - {s.pop()})