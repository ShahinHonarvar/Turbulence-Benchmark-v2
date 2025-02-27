def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(90, 200):
        if s[i] in s[i + 1:200] and s[i] not in repeat_chars:
            repeat_chars.add(s[i])
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
    return result