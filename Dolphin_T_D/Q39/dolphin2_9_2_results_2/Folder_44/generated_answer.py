def return_n_greatest_chars(string):
    return sorted([ch for ch in string if ch.isalpha()], key=lambda x: -ord(x))[:73]