def return_n_greatest_chars(s):
    return sorted([char for char in sorted(s, reverse=True)[:3]])