def return_nth_smallest_ascii(s):
    chars = sorted(s[34:69])
    return sorted(chars, key=ord)[5]