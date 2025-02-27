def return_n_greatest_chars(text):
    return sorted([ord(c) for c in text], reverse=True)[:2]