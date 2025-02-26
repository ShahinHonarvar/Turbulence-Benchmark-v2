def return_n_greatest_chars(s):
    sorted_chars = sorted(list(set(s)), key=ord, reverse=True)[:34]
    return sorted(sorted_chars)