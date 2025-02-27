def return_nth_smallest_ascii(s):
    substring = s[28:55]
    return sorted(substring, key=lambda x: ord(x))[13]