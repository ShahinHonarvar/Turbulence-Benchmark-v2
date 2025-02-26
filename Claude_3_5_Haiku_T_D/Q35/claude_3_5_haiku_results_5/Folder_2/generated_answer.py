def remove_repeat_chars(s):
    if len(s) <= 93:
        return s
    segment = s[73:93]
    repeat_chars = set((char for char in segment if segment.count(char) > 1))
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)