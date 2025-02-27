def return_n_greatest_chars(text):
    return sorted(sorted(text, reverse=True, key=ord)[:20])