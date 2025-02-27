def return_n_greatest_chars(s):
    return sorted(sorted(list(set(s))), key=lambda x: ord(x), reverse=True)[:49]