def return_n_smallest_chars(s):
    return sorted([c for c in s] * (90 // len(s) + 1))[:90][::-1]