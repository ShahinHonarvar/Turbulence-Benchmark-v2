def return_nth_smallest_ascii(text):
    subset = text[51:90]
    sorted_chars = sorted(set(subset), key=lambda c: ord(c))
    return sorted_chars[13]