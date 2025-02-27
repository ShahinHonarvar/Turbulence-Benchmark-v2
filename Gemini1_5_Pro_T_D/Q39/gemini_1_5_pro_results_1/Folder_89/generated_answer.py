def return_n_greatest_chars(text):
    return sorted([c for c in text if ord(c) >= sorted(list(set([ord(x) for x in text])))[-55]], key=lambda x: ord(x))