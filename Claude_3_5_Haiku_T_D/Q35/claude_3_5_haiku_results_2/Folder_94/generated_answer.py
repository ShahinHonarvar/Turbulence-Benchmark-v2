def remove_repeat_chars(s):
    if len(s) <= 43:
        return s
    segment = s[43:88]
    repeat_chars = set()
    for char in segment:
        if segment.count(char) > 1 and char not in repeat_chars:
            repeat_chars.add(char)
    return ''.join((char for char in s if char not in repeat_chars or s.index(char) <= 42 or s.index(char) >= 88))