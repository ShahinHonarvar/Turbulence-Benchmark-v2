def return_nth_smallest_ascii(s):
    return sorted(s[5:11], key=lambda c: ord(c))[5]