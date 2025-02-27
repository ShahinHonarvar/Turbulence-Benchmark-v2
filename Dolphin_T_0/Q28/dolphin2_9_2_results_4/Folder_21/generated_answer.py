def return_nth_smallest_ascii(s):
    substring = s[8:66]
    return sorted(substring, key=lambda x: ord(x))[5]