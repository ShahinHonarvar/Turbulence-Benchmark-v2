def remove_repeat_chars(s):
    if len(s) <= 19:
        return s
    segment = s[19:60]
    repeat_chars = set()
    for char in segment:
        if segment.count(char) > 1 and char not in repeat_chars:
            repeat_chars.add(char)
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
        elif s.index(char) < 19 or s.index(char) >= 60:
            result.append(char)
    return ''.join(result)