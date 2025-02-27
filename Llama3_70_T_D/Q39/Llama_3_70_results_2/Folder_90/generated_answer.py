def return_n_greatest_chars(s):
    return sorted(s, key=lambda x: (x in s[:24], ord(x)))[::-1][:24]