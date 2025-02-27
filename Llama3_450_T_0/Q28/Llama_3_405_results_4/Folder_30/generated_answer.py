def return_nth_smallest_ascii(s):
    chars = sorted(s[50:77])
    return sorted(chars, key=lambda x: ord(x))[10]