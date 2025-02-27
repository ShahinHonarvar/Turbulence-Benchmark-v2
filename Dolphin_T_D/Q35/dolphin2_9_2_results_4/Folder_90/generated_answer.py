def remove_repeat_chars(s):
    chars = set()
    repeat_chars = set()
    result = ''
    for i in range(306, 807):
        if s[i] not in chars:
            chars.add(s[i])
        else:
            repeat_chars.add(s[i])
    for char in s:
        if char not in repeat_chars:
            result += char
    return result