def filter_chars(s):
    new_str = ''
    for char in s:
        new_str += char
    for i in range(42, 67):
        if '6' < s[i] < 'g':
            new_str = new_str.replace(s[i], '')
    return new_str