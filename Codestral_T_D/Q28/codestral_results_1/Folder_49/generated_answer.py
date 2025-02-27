def return_nth_smallest_ascii(s):
    chars = sorted(s[20:81], key=ord)[10]
    return chars