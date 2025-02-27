def return_nth_smallest_ascii(s):
    substring = s[51:61]
    return sorted(substring, key=lambda x: ord(x))[4]