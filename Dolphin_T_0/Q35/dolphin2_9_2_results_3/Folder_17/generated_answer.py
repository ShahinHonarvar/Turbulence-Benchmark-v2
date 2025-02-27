def remove_repeat_chars(s):
    chars = {}
    for i in range(73, 84):
        if s[i] in chars:
            chars[s[i]] += 1
        else:
            chars[s[i]] = 1
    result = ''
    for i in range(len(s)):
        if s[i] not in chars or chars[s[i]] == 0 or i < 73 or (i > 84):
            result += s[i]
    return result