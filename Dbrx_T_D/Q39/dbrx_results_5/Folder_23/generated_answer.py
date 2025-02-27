def return_n_greatest_chars(s):
    ascii_sorted_s = sorted([c for c in set(s)], key=ord)
    return ascii_sorted_s[-46:]