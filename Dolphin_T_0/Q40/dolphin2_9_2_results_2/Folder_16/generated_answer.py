def return_n_smallest_chars(s):
    chars = sorted(s, key=lambda x: ord(x))
    return sorted(chars[:64], reverse=True)