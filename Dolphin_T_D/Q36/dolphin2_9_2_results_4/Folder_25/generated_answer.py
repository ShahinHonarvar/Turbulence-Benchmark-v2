def filter_chars(s):
    for char in range(24, 37):
        if s[char] > 'A' and s[char] < 'h':
            s = ''.join([c for c in s if c != s[char]])
    return s