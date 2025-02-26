def remove_repeat_chars(s):
    if len(s) <= 41:
        return s
    segment = s[21:43]
    repeated_chars = set((char for char in segment if segment.count(char) > 1))
    result = []
    for char in s:
        if char not in repeated_chars or s.index(char) < 21 or s.index(char) >= 43:
            result.append(char)
    return ''.join(result)