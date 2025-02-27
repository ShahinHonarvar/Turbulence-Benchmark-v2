def return_nth_smallest_ascii(s):
    chars = sorted([s[i] for i in range(10)])
    return chars[9]