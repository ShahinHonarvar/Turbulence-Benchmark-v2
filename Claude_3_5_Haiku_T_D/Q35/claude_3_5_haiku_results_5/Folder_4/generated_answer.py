def remove_repeat_chars(s):
    if len(s) <= 74:
        return s
    segment = s[50:74]
    repeat_chars = set()
    for char in segment:
        if segment.count(char) > 1 and char not in repeat_chars:
            repeat_chars.add(char)
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) < 50 or s.index(char) >= 74))
    return result