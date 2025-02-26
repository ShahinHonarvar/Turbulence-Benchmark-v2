def return_n_greatest_chars(s):
    sorted_chars = sorted(list(set(s)), reverse=True)[:14]
    return sorted(sorted_chars)