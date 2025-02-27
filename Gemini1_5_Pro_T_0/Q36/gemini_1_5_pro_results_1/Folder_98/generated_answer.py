def filter_chars(s):
    temp = list(s)
    for i in range(4, 8):
        if s[i] > '1' and s[i] < 'J':
            c = s[i]
            for j in range(len(temp)):
                if temp[j] == c:
                    temp[j] = ''
    return ''.join(temp)