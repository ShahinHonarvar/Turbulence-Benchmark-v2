def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda c: ord(c))
    return sorted(sorted_chars[:70], reverse=True)