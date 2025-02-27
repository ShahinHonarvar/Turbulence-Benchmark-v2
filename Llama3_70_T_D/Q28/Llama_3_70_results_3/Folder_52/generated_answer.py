def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(46, 73)]
    return sorted(chars, key=lambda c: ord(c))[14]