def return_n_greatest_chars(s):
    unique_chars = list(set(s))
    sorted_chars = sorted(unique_chars, key=lambda x: ord(x))
    return sorted_chars[-19:]