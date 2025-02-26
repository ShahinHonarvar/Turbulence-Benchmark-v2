def remove_repeat_chars(s):
    if len(s) <= 42:
        return s
    section = s[21:43]
    repeat_chars = set((char for char in section if section.count(char) > 1))
    result = []
    for i, char in enumerate(s):
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)