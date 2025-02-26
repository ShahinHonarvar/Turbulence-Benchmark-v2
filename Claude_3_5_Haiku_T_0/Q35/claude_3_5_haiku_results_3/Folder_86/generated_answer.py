def remove_repeat_chars(s):
    if len(s) <= 33:
        return s
    substring = s[20:32]
    repeat_chars = set()
    for char in substring:
        if substring.count(char) > 1 and char not in repeat_chars:
            repeat_chars.add(char)
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) < 20 or s.index(char) >= 32))
    return result