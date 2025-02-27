def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if s[i] > 'A' and s[i] < 'U':
            if i not in range(70, 74):
                result += s[i]
        else:
            result += s[i]
    return result