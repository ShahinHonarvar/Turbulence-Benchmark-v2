def return_n_greatest_chars(s):
    sorted_s = sorted(s, key=ord, reverse=True)
    return sorted(sorted_s[:23])