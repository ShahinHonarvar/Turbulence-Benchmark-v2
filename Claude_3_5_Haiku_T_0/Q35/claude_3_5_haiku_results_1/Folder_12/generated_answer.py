def remove_repeat_chars(s):
    if len(s) <= 16:
        return s
    segment = s[17:87]
    repeat_chars = set()
    for char in segment:
        if segment.count(char) > 1 and char not in repeat_chars:
            repeat_chars.add(char)
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
        elif s.index(char) < 17 or s.index(char) >= 87:
            result.append(char)
    return ''.join(result)