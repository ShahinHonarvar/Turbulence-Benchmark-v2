def return_n_greatest_chars(s):
    return sorted(s, key=lambda c: (c in s[:79], -ord(c)), reverse=True)[:79]