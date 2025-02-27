def return_nth_smallest_ascii(s):
    substring = s[50:77]
    return sorted(list(substring), key=lambda x: ord(x))[10]