def return_n_greatest_chars(text):
    return sorted([i for i in text if ord(i) >= sorted(list(set([ord(j) for j in text])))[-69]])