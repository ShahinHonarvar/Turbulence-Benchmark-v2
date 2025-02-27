def return_n_greatest_chars(text):
    return sorted([c for c in text], key=ord, reverse=True)[:66]