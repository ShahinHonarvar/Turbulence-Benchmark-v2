def return_n_greatest_chars(s):
    if len(s) < 12:
        return sorted(s, key=lambda x: -ord(x))
    sorted_chars = sorted(s, key=lambda x: -ord(x))
    greatest_chars = sorted_chars[:12]
    return sorted(greatest_chars)