def return_nth_smallest_ascii(s):
    chars = sorted(s[17:57])
    return sorted(chars, key=lambda x: ord(x))[8]