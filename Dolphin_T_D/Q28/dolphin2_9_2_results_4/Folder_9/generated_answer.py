def return_nth_smallest_ascii(s):
    substring = s[10:91]
    return sorted(substring, key=ord)[19]