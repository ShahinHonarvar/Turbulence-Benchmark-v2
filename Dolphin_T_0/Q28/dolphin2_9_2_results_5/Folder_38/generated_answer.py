def return_nth_smallest_ascii(s):
    chars = [(s[i], i) for i in range(46) if s[i] in s[46:]]
    chars.sort()
    return chars[9][0]