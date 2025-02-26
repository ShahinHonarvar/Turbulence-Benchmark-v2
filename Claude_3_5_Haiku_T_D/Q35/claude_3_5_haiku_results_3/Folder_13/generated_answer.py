def remove_repeat_chars(s):
    if len(s) <= 46:
        return s
    substring = s[47:91]
    seen_chars = set()
    repeat_chars = set()
    for char in substring:
        if char in seen_chars:
            repeat_chars.add(char)
        else:
            seen_chars.add(char)
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) < 47 or s.index(char) >= 91))
    return result