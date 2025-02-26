def return_n_greatest_chars(s):
    sorted_chars = sorted(set(s), key=lambda x: ord(x), reverse=True)
    return sorted_chars[:52] if len(sorted_chars) >= 52 else sorted_chars