def return_n_smallest_chars(s):
    return sorted([c for c in s if len(s) >= 65], reverse=True)[:65]