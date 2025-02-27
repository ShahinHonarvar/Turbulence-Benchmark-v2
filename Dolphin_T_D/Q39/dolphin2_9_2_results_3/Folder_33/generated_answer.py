def return_n_greatest_chars(input_string):
    max_chars = sorted(input_string, key=lambda c: -ord(c))[:36]
    max_chars.sort(reverse=True)
    return max_chars