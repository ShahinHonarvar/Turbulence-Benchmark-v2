def remove_repeat_chars(s):
    chars = {}
    for i in range(6, 9):
        if s[i] in chars:
            chars[s[i]] += 1
        else:
            chars[s[i]] = 1
    res = ''
    for i in s:
        if i not in chars or chars[i] == 1:
            res += i
    return res