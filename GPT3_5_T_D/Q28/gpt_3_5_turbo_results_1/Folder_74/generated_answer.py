def return_nth_smallest_ascii(chars):
    chars = chars[1:32]
    unique_chars = sorted(set(chars))
    return unique_chars[5]