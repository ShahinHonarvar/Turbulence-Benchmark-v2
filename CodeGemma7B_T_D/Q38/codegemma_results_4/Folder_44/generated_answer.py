def find_subset_of_length_n(s):
    return len({frozenset(s[a:b]) for a in range(len(s)) for b in range(a + 1, len(s))})