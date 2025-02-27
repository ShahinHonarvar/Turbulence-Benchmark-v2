def return_n_greatest_chars(text):
    return sorted([char for char in text if char.isalnum()], key=ord, reverse=True)[:36]