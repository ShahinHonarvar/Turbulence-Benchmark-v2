def return_nth_smallest_ascii(txt):
    chars = txt[34:82]
    sorted_chars = sorted(chars, key=lambda c: ord(c))
    return sorted_chars[11]