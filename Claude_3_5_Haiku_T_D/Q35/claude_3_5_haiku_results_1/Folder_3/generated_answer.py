def remove_repeat_chars(s):
    if len(s) <= 56:
        return s
    substr = s[57:88]
    repeat_chars = set()
    for char in substr:
        if substr.count(char) > 1:
            repeat_chars.add(char)
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) < 57 or s.index(char) >= 88))
    return result