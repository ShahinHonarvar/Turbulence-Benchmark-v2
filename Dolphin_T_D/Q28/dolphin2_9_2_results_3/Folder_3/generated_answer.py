def return_nth_smallest_ascii(s):
    chars = s[25:45]
    return sorted(chars, key=lambda x: ord(x))[10]