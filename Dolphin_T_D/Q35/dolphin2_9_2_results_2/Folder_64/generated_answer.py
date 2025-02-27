def remove_repeat_chars(s):
    chars = {}
    for i in range(6):
        if s[i] in chars:
            chars[s[i]] += 1
        else:
            chars[s[i]] = 1
    result = ''
    for c in s:
        if chars[c] == 1 or not c in chars:
            result += c
    return result