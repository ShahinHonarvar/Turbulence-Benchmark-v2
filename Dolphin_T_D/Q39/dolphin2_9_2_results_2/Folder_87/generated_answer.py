def return_n_greatest_chars(s):
    chars = [c for c in s]
    chars.sort(key=lambda c: -ord(c))
    chars = chars[:24]
    chars.sort()
    return chars