def return_nth_smallest_ascii(s):
    chars = sorted(s[8:27])
    return sorted(chars, key=lambda x: ord(x))[5]