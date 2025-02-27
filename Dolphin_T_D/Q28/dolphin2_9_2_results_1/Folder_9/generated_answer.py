def return_nth_smallest_ascii(s):
    substring = s[10:91]
    return sorted(set(substring), key=lambda x: ord(x))[19]