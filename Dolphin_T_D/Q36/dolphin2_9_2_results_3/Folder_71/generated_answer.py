def filter_chars(s):
    for i in range(82, 89):
        c = s[i]
        if '*' < c < '[':
            s = ''.join([char for char in s if char != c])
    return s