def find_subset_of_length_n(s):
    if len(s) < 22:
        return 0
    l = list(s)
    return len([l[i:j] for i in range(len(l)) for j in range(i + 22, len(l) + 1)])