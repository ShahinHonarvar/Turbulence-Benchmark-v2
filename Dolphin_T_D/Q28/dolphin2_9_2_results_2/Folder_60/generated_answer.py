def return_nth_smallest_ascii(s):
    ascii_chars = sorted([s[i] for i in range(36, 80)])
    return ascii_chars[11]