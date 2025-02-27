def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x))
    n_greatest_chars = sorted_chars[-73:]
    n_greatest_chars.sort()
    return n_greatest_chars