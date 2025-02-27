def return_n_greatest_chars(s):
    return sorted(sorted(s, key=lambda x: -ord(x))[:37])