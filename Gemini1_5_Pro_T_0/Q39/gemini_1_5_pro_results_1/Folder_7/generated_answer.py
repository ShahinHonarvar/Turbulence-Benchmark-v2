def return_n_greatest_chars(text):
    return sorted([char for char in sorted(text, key=ord, reverse=True)][:49])