def return_n_greatest_chars(a_string):
    alphabet = list(a_string)
    alphabet.sort(reverse=True)
    return alphabet[:44]