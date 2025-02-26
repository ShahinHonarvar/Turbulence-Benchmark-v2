def remove_repeat_chars(s):
    if len(s) <= 2:
        return s
    repeat_chars = set()
    for char in s[1:-1]:
        if s[1:-1].count(char) > 1:
            repeat_chars.add(char)
    result = s[0]
    for char in s[1:-1]:
        if char not in repeat_chars:
            result += char
    result += s[-1]
    return result