def remove_repeat_chars(s):
    chars = {}
    for i in range(44, 78):
        chars[s[i]] = chars.get(s[i], 0) + 1
    result = ''
    for c in s:
        if c not in chars:
            result += c
    return result