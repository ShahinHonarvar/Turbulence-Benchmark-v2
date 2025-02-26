def remove_repeat_chars(s):
    if len(s) <= 6:
        return s
    segment = s[7:9]
    repeat_chars = set((char for char in segment if segment.count(char) > 1))
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)