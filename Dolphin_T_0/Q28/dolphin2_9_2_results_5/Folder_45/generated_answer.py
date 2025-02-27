def return_nth_smallest_ascii(string):
    chars = string[0:16]
    sorted_chars = sorted(chars, key=lambda x: ord(x))
    return sorted_chars[15]