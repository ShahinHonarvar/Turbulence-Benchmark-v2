def find_subset_of_length_n(s):
    if len(s) < 94:
        return 0
    total = 0
    for i in range(len(s)):
        total += find_subset_of_length_n(s - {s[i]})
    return total