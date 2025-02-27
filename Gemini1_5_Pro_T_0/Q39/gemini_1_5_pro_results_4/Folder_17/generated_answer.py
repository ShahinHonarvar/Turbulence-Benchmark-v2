def return_n_greatest_chars(text: str):
    sorted_chars = sorted(text)
    return sorted_chars[-11:]