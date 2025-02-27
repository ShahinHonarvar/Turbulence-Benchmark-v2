def remove_repeat_chars(s):
    chars = {}
    for i in s[55:84]:
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    result = ''
    for i in s:
        if i not in chars or chars[i] == 1:
            result += i
    return result