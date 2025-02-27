def filter_chars(s):
    temp = ''
    for i in range(len(s)):
        if not (51 < i < 76 and '5' < s[i] < 'f'):
            temp += s[i]
    return temp