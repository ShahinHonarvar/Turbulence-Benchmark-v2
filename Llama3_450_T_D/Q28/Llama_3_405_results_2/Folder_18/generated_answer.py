def return_nth_smallest_ascii(s):
    chars = sorted(s[51:61])
    return sorted(chars, key=lambda x: ord(x))[4]