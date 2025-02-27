def filter_chars(s):
    result = s[:51] + ''.join((c for c in s[51:77] if c <= '5' or c >= 'f')) + s[77:]
    return result