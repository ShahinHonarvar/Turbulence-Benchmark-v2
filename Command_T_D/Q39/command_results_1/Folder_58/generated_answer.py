def return_n_greatest_chars(s):
    return sorted(set(s), key=lambda x: x.lower(), reverse=True)[:49]