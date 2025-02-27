def return_n_greatest_chars(s):
    s_sorted = sorted(s)
    n_greatest_chars = s_sorted[-82:][::-1]
    return n_greatest_chars