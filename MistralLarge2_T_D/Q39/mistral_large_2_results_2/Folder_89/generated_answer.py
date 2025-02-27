def return_n_greatest_chars(s):
    return sorted([char for char in s if len(s) >= 55], key=lambda x: -ord(x))[:55]