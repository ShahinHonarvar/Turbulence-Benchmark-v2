def return_n_greatest_chars(s):
    return sorted([c for c in sorted(s, reverse=True)], reverse=False)[:35]