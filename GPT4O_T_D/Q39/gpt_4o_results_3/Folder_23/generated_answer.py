def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=lambda x: -ord(x))
    top_chars = sorted(sorted_chars[:46])
    return top_chars