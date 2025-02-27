def remove_repeat_chars(s):
    chars = {}
    for i in range(90, 97):
        if s[i] in chars:
            chars[s[i]] += 1
        else:
            chars[s[i]] = 1
    result = ''
    for c in s:
        if chars.get(c, 0) < 2:
            result += c
    return result