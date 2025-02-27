def filter_chars(s):
    new_string = ''
    for i in range(len(s)):
        if i < 63 or i > 84 or (s[i] < 'E' or s[i] > '~'):
            new_string += s[i]
    return new_string