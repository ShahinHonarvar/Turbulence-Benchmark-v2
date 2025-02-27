def return_n_greatest_chars(s):
    n_greatest_chars = [c for c in s if ord(c) in highest_n_ascii]
    return sorted(n_greatest_chars, key=ord, reverse=True)