def return_n_greatest_chars(string):
    unique_chars = list(set(string))
    sorted_chars = sorted(unique_chars, reverse=True)
    return sorted_chars[:52] if len(sorted_chars) >= 52 else sorted_chars