def return_n_smallest_chars(s):
    return sorted([c for c in s] * (52 // len(s) + 1))[:52][::-1]