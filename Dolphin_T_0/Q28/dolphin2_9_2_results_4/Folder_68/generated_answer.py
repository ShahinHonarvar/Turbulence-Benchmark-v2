def return_nth_smallest_ascii(s):
    return sorted(s[0:11], key=lambda x: ord(x))[10]