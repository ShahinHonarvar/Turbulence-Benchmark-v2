def return_nth_smallest_ascii(s):
    return sorted(s[14:67], key=lambda x: ord(x))[7]