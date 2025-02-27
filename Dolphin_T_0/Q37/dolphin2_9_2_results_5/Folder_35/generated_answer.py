def filter_chars(s):
    new_s = ''
    for i in range(len(s)):
        if i < 155 or i > 403 or s[i] < '(' or (s[i] > ']'):
            new_s = new_s + s[i]
    return new_s