def return_nth_smallest_ascii(s):
    return sorted(s[38:83], key=lambda x: ord(x))[19]