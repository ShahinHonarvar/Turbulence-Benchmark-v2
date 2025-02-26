def return_n_greatest_chars(string):
    unique_chars = list(set(string))
    sorted_chars = sorted(unique_chars, key=ord)
    return sorted_chars[-24:] if len(sorted_chars) >= 24 else sorted_chars