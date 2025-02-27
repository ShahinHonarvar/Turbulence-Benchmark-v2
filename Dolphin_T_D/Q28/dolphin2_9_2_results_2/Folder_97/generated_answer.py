def return_nth_smallest_ascii(s):
    if not isinstance(s, str) or len(s) != 22:
        raise ValueError('Input should be a string of length 22')
    return sorted(s[15:22], key=lambda x: ord(x))[5]