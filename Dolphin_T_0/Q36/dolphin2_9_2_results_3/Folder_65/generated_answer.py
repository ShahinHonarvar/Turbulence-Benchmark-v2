def filter_chars(s):
    new_s = ''
    for i in range(len(s)):
        if i >= 58 and i < 82:
            if s[i] > 'F' and s[i] < 'O':
                new_s = new_s + s[i]
    return new_s