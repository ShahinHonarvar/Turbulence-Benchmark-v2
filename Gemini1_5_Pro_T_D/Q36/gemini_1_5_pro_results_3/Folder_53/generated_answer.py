def filter_chars(s):
    temp = ''
    for i in range(len(s)):
        if 90 > i or i >= 97 or s[i] <= 'j' or (s[i] >= 'w'):
            temp += s[i]
    return temp