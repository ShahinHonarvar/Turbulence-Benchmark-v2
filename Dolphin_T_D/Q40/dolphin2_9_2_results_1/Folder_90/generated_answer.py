def return_n_smallest_chars(s):
    return sorted([c for c in s] * (24 // len(s) + 1), key=lambda c: ord(c), reverse=True)[:24]