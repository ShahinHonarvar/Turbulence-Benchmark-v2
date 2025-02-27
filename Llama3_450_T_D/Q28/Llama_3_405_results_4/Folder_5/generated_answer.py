def return_nth_smallest_ascii(s):
    chars = sorted(s[5:90], key=lambda x: ord(x))
    return chars[12]