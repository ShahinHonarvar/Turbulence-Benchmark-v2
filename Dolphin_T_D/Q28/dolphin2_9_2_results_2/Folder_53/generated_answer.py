def return_nth_smallest_ascii(s):
    substring = s[40:61]
    return sorted(substring, key=lambda x: ord(x))[18]