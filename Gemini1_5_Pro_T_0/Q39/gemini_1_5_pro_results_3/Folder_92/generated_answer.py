def return_n_greatest_chars(text):
    return sorted([c for c in sorted(text, reverse=True)[:63]])