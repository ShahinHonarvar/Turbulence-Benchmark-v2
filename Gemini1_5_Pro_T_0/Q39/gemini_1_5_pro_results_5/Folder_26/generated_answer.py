def return_n_greatest_chars(text):
    return sorted([c for c in text if ord(c) >= sorted(list(set(map(ord, text))))[-43]], key=ord)