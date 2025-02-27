def return_n_greatest_chars(text: str):
    sorted_chars = sorted(text, key=ord, reverse=True)
    return sorted_chars[:13]