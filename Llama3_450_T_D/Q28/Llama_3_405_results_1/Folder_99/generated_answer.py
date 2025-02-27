def return_nth_smallest_ascii(s):
    chars = sorted(s[17:66])
    ascii_sorted = sorted(chars, key=lambda x: ord(x))
    return ascii_sorted[7]