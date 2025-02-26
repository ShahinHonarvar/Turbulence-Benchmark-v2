def remove_repeat_chars(s):
    if len(s) <= 11:
        return s
    start = 11
    end = min(100, len(s))
    substring = s[start:end]
    chars_to_remove = set((char for char in substring if substring.count(char) > 1))
    result = []
    for i, char in enumerate(s):
        if i < start or i >= end:
            result.append(char)
        elif char not in chars_to_remove:
            result.append(char)
    return ''.join(result)