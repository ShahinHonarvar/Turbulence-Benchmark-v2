def return_n_smallest_chars(s):
    return sorted([c for c in s if ord(c) >= 0 and ord(c) <= 127], reverse=True)[:52]