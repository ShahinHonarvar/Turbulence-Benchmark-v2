def return_nth_smallest_ascii(s):
    sub = s[17:46]
    return sorted(sub, key=lambda x: ord(x))[6]