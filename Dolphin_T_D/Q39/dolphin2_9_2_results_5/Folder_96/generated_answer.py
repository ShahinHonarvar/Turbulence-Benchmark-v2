def return_n_greatest_chars(s):
    sorted_chars = sorted([c for c in s], reverse=True)
    return sorted_chars[:20]