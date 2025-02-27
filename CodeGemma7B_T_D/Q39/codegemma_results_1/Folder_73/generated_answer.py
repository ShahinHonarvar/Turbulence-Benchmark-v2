def return_n_greatest_chars(message):
    greatest_chars = sorted(message, key=ord, reverse=True)[:80]
    return greatest_chars