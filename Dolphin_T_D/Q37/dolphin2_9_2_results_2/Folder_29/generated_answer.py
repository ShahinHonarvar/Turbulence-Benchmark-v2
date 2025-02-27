def filter_chars(s):
    outputStr = ''
    for i in range(len(s)):
        if i < 12 or i > 88:
            outputStr += s[i]
        elif s[i] >= '&' and s[i] <= 'v':
            pass
        else:
            outputStr += s[i]
    return outputStr