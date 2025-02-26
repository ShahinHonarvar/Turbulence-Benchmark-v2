def return_n_greatest_chars(string):
    unique_chars = sorted(set(string), key=lambda x: ord(x), reverse=True)[:40]
    return sorted(unique_chars)