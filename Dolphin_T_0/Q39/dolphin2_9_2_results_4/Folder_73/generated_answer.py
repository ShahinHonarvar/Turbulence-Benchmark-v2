def return_n_greatest_chars(s):
    max_chars = sorted([char for char in s], reverse=True)[:80]
    return sorted(max_chars)