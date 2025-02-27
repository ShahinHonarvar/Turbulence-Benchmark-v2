def return_n_smallest_chars(s):
    return sorted(s, key=lambda x: ord(x) if len(s) >= 46 else s[:46])[:46]