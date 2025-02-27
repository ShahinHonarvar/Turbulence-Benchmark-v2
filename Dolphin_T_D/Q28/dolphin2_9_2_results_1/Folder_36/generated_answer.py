def return_nth_smallest_ascii(s):
    substring = s[17:57]
    return sorted(substring, key=lambda x: ord(x))[9]