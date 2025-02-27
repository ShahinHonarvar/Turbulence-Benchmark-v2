def filter_chars(s):
    bc = [s[i] for i in range(len(s)) if not ('!' < s[i] < 'A' and 11 <= i < 46)]
    return ''.join(bc)