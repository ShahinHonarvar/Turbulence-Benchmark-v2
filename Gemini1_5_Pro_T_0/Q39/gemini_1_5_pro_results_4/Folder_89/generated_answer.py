def return_n_greatest_chars(text):
    return sorted([c for c in text if ord(c) >= sorted(list(map(ord, text)))[-55]], reverse=False)