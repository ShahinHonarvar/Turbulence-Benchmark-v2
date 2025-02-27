def return_n_greatest_chars(s):
    return sorted(s, key=lambda x: (x in s[:28], -ord(x)))[-28:][::-1]