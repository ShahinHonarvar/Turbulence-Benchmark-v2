def return_nth_smallest_ascii(string):
    chars = string[8:27]
    sorted_chars = sorted(chars, key=lambda x: ord(x))
    return sorted_chars[5]