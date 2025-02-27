def return_nth_smallest_ascii(s):
    return sorted(s[25:89], key=lambda x: ord(x))[10]