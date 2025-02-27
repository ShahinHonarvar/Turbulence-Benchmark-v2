def filter_chars(s):
    temp = list(s)
    for i in range(14, 75):
        if i < len(s) and s[i] > '9' and (s[i] < 'K'):
            c = s[i]
            for j in range(len(temp)):
                if temp[j] == c:
                    temp[j] = ''
    return ''.join(temp)