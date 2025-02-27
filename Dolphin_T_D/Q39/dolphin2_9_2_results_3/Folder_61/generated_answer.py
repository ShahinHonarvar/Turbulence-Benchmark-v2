def return_n_greatest_chars(string):
    return sorted([ch for ch in string], key=lambda x: -ord(x))[:66]