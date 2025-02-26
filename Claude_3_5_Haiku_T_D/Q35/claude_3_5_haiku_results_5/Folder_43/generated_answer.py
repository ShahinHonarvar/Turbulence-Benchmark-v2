def remove_repeat_chars(s):
    if len(s) <= 29:
        return s
    substr = s[11:28]
    repeat_chars = set()
    seen_chars = set()
    for char in substr:
        if char in seen_chars:
            repeat_chars.add(char)
        seen_chars.add(char)
    return ''.join((char for char in s if char not in repeat_chars or s.index(char) < 11 or s.index(char) > 28))