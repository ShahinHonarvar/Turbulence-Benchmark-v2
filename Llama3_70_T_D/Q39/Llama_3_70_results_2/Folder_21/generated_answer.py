def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=lambda x: (x, -ord(x)), reverse=True)[:44]
    return sorted_chars