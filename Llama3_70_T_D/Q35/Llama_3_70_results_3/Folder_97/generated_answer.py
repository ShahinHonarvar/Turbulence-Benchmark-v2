def remove_repeat_chars(s):
    repeat_chars = set()
    for char in s[34:69]:
        if s.count(char) > 1:
            repeat_chars.add(char)
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
    return result