def return_n_greatest_chars(string):
    unique_chars = list(set(string))
    sorted_chars = sorted(unique_chars, key=lambda x: ord(x))
    return sorted_chars[-10:] if len(sorted_chars) >= 10 else sorted_chars