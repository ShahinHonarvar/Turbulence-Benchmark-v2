def return_n_greatest_chars(text):
    return sorted([c for c in text], reverse=True)[:23]