def filter_chars(s):
    new_s = ''
    for i in range(len(s)):
        if not (29 <= i <= 97 and '-' <= s[i] <= 'n'):
            new_s += s[i]
    return new_s