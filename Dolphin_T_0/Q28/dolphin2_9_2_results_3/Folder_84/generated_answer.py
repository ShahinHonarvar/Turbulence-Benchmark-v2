def return_nth_smallest_ascii(s):
    substring = s[52:80]
    return sorted(substring, key=lambda x: ord(x))[6]