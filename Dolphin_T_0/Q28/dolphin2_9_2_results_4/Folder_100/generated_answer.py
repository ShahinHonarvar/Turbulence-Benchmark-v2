def return_nth_smallest_ascii(s):
    sub = s[5:48]
    unique = ''.join(sorted(set(sub), key=lambda c: ord(c)))
    return unique[12]