def return_n_greatest_chars(s):
    sorted_chars = sorted(s, reverse=True)[:8]
    sorted_chars.sort()
    return sorted_chars