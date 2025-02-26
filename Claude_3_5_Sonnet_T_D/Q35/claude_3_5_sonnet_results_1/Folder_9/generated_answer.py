def remove_repeat_chars(s):
    if len(s) <= 81:
        return s
    start = 81
    end = min(200, len(s))
    substring = s[start:end]
    repeated_chars = set((char for char in substring if substring.count(char) > 1))
    result = []
    for i, char in enumerate(s):
        if i < start or i >= end or char not in repeated_chars:
            result.append(char)
    return ''.join(result)