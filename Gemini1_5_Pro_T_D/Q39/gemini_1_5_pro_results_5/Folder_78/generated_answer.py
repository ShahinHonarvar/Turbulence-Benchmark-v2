def return_n_greatest_chars(text):
    return sorted([c for c in text if ord(c) >= sorted(list(set([ord(t) for t in text])))[-43]], reverse=True)