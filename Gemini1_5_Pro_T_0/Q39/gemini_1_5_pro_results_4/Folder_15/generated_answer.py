def return_n_greatest_chars(text):
    return sorted([c for c in text if ord(c) >= sorted(list(set([ord(x) for x in text])))[-57]], key=ord)