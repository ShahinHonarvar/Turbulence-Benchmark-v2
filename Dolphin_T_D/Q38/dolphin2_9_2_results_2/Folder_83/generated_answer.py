def find_subset_of_length_n(s):
    if len(s) < 95:
        return 0
    n = len(s)
    res = 0
    for i in range(95):
        res = res + find_subset_of_length_n(s - {s[i]})
    return res + 1