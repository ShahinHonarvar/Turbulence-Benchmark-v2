def return_nth_smallest_ascii(string):
    chars = list(string[46:83])
    sorted_chars = sorted(chars, key=lambda x: ord(x))
    return sorted_chars[15]