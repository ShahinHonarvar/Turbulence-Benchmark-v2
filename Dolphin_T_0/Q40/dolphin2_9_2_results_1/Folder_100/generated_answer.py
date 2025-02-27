def return_n_smallest_chars(s):
    return sorted([c for c in s] + [''] * 72, key=lambda c: ord(c), reverse=True)[:72]