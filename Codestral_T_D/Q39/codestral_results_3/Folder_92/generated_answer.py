def return_n_greatest_chars(s):
    return sorted(sorted(list(set(s)))[-63:])