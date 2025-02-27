def return_n_greatest_chars(text):
    return sorted(sorted(list(text), reverse=True)[:12])