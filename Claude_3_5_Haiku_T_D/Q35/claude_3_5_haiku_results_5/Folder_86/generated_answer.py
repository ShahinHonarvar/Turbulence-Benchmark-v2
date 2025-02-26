def remove_repeat_chars(s):
    if len(s) <= 20:
        return s
    segment = s[20:32]
    repeat_chars = set()
    for char in segment:
        if segment.count(char) > 1 and char not in repeat_chars:
            repeat_chars.add(char)
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
        elif s.index(char) < 20 or s.index(char) >= 32:
            result += char
    return result