def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 12 or i > 77 or s[i] < ':' or (s[i] > 'L'):
            result += s[i]
    return result