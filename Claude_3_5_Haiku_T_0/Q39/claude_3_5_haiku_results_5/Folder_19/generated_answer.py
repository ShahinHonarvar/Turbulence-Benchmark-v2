def return_n_greatest_chars(s):
    sorted_chars = sorted(set(s), key=lambda x: ord(x), reverse=True)[:58]
    return sorted(sorted_chars)