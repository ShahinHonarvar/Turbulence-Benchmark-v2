def remove_repeat_chars(s):
    if len(s) <= 29:
        return s
    substring = s[11:28]
    repeat_chars = set()
    for char in substring:
        if substring.count(char) > 1 and char not in repeat_chars:
            repeat_chars.add(char)
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) < 11 or s.index(char) > 28))
    return result