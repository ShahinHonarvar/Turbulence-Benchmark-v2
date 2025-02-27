def filter_chars(s):
    for ch in range(81, 89):
        if s[ch] > 'f' and s[ch] < '{':
            s = ''.join([char for char in s if char != s[ch]])
    return s