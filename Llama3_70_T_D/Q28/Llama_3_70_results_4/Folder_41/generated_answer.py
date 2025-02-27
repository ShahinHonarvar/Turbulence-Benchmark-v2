def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(58, 86)]
    unique_chars = sorted(set(chars))
    return unique_chars[18]