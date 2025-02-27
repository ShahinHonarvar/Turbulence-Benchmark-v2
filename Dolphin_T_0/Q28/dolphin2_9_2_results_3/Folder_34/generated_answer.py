def return_nth_smallest_ascii(s):
    return s[sorted(range(19), key=lambda x: s[x])[18]]