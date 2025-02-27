def return_nth_smallest_ascii(s):
    chars = sorted(s[:4])
    return sorted(chars, key=lambda x: ord(x))[3]