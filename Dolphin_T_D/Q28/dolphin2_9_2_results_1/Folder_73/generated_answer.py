def return_nth_smallest_ascii(s):
    chars = sorted(s[0:70], key=lambda x: ord(x))
    return chars[9]