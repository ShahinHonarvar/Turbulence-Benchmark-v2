def filter_chars(s):
    for i in range(3, 5):
        c = s[i]
        if c > 'Y' and c < 's':
            s = ''.join([char for char in s if char != c])
    return s