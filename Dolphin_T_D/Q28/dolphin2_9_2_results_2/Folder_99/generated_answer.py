def return_nth_smallest_ascii(s):
    chars = s[17:66]
    return sorted(chars, key=lambda x: ord(x))[7]