def filter_chars(s):
    res = ''
    for i in range(len(s)):
        if i > 54 and i < 92 and (s[i] > 'J') and (s[i] < 'X'):
            temp = s[i]
            res = ''
            for char in s:
                if char != temp:
                    res += char
            s = res
        else:
            res += s[i]
    return res