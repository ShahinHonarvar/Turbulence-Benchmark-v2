def return_nth_smallest_ascii(s):
    chars = s[3:27]
    return sorted(set(chars), key=lambda x: ord(x))[4]