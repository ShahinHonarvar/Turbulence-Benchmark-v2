def filter_chars(s):
    chars_to_filter = [s[i] for i in range(24, 37) if s[i] > 'A' and s[i] < 'h']
    for c in chars_to_filter:
        s = ''.join([x for x in s if x != c])
    return s