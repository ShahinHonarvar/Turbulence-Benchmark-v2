def return_n_greatest_chars(text):
    return sorted([x for x in text if ord(x) >= sorted(list(set([ord(c) for c in text])))[-84]])