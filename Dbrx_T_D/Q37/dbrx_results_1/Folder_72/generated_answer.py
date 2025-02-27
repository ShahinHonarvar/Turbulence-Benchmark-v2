def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 35 or i > 51 or (s[i] < 'H' or s[i] > 's'):
            result += s[i]
    return result