def return_n_greatest_chars(s):
    sorted_s = sorted(s, reverse=True)
    n_greatest_chars = [char for char in sorted(sorted_s[:80])]
    return n_greatest_chars