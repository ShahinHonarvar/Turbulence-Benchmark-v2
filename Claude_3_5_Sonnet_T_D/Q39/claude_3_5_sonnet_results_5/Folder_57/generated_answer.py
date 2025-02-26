def return_n_greatest_chars(s):
    return sorted(list(set(s)), reverse=True)[:29]