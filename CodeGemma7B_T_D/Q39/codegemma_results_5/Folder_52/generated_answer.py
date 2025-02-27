def return_n_greatest_chars(text):
    greatest_chars = sorted([char for char in text], key=ord, reverse=True)[:68]
    return greatest_chars