def return_nth_smallest_ascii(s):
    substring = s[14:36]
    return sorted(substring, key=lambda x: ord(x))[10]