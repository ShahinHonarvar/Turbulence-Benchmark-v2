def remove_repeat_chars(s):
    if len(s) <= 23:
        return s
    repeat_chars = set()
    for char in s[23:24]:
        if s[23:24].count(char) > 1:
            repeat_chars.add(char)
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
    return result