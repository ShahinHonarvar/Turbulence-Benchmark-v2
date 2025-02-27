def return_n_greatest_chars(text):
    return sorted([i for i in text], key=ord, reverse=True)[:36]