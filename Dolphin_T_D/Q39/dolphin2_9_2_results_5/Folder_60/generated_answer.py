def return_n_greatest_chars(s):
    chars = [c for c in s if c.isalpha()]
    chars = sorted(chars, key=lambda c: ord(c), reverse=True)
    return chars[:28][::-1]