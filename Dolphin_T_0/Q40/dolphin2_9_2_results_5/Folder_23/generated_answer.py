def return_n_smallest_chars(string):
    chars = sorted(list(string), key=lambda c: ord(c), reverse=False)[:46]
    return sorted(chars)