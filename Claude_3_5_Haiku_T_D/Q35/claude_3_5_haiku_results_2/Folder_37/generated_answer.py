def remove_repeat_chars(s):
    if len(s) <= 4:
        return s
    segment = s[3:7]
    repeat_chars = set((char for char in segment if segment.count(char) > 1))
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
        elif s.index(char) < 3 or s.index(char) >= 7:
            result.append(char)
    return ''.join(result)