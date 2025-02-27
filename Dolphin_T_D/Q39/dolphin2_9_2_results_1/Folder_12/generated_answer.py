def return_n_greatest_chars(s):
    s = list(s)
    sorted_s = sorted(s, key=lambda x: -ord(x))
    return sorted_s[:61]