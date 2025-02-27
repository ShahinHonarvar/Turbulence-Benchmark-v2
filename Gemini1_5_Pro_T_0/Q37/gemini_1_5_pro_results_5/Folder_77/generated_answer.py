def filter_chars(s):
    for i in range(384, 412):
        if i < len(s) and '/' <= s[i] <= '8':
            c = s[i]
            s = ''.join((x for x in s if x != c))
    return s