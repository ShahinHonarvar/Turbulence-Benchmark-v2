def return_n_greatest_chars(text):
    return sorted([c for c in text if ord(c) >= sorted(list(set([ord(i) for i in text])))[-57]], key=ord)