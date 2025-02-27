def return_nth_smallest_ascii(s):
    chars = s[0:5]
    return sorted(chars, key=ord)[4]