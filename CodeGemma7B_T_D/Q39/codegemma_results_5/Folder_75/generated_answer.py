def return_n_greatest_chars(text):
    greatest_two_chars = sorted(set(text), key=ord, reverse=True)[:2]
    return greatest_two_chars