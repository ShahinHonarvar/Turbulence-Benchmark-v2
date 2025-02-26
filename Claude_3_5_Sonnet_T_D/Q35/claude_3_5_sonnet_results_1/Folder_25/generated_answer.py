def remove_repeat_chars(s):
    if len(s) <= 38:
        return s
    section = s[38:43]
    repeats = set((char for char in section if section.count(char) > 1))
    result = []
    for i, char in enumerate(s):
        if char not in repeats or (i >= 38 and i < 43):
            result.append(char)
    return ''.join(result)