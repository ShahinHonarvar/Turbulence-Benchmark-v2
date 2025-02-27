def filter_chars(s):
    temp = ''
    for i in range(len(s)):
        if 38 < i < 81 and '.' < s[i] < '^':
            continue
        else:
            temp += s[i]
    return temp