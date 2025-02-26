def remove_repeat_chars(s):
    if len(s) <= 11:
        return s
    end = min(100, len(s))
    substring = s[10:end]
    chars_to_remove = set((char for char in substring if substring.count(char) > 1))
    result = []
    for i, char in enumerate(s):
        if i < 10 or i >= 100 or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)