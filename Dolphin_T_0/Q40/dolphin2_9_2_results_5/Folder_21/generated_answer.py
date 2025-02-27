def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda c: ord(c))[:44]
    sorted_chars.sort(key=lambda c: ord(c), reverse=True)
    return sorted_chars