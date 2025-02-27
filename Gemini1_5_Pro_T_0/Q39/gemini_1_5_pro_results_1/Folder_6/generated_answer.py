def return_n_greatest_chars(text):
    return sorted([c for c in text if ord(c) >= sorted(list(set([ord(i) for i in text])))[-47]], reverse=True)[:47]