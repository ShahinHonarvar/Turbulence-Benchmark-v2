def return_n_greatest_chars(s):
    sorted_chars = sorted(set(s), reverse=True)[:84]
    sorted_chars.sort()
    return sorted_chars