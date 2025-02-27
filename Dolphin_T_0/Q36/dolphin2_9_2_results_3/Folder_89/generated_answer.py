def filter_chars(s):
    for ch in range(57, 69):
        if s[ch] > '(' and s[ch] < 'W':
            s = ''.join([char for char in s if char != s[ch]])
    return s