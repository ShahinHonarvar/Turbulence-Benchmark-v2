def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 722 or i > 832 or s[i] < 'K' or (s[i] > 'm'):
            result += s[i]
    return result