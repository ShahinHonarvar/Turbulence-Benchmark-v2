def return_n_greatest_chars(s):
    sorted_chars = sorted([c for c in s], reverse=True)[:35]
    return sorted(sorted_chars)