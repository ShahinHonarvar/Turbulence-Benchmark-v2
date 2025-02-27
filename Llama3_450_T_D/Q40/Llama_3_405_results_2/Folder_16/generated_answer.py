def return_n_smallest_chars(s):
    return sorted([c for c in s] * (64 // len(s) + 1))[:64][::-1]