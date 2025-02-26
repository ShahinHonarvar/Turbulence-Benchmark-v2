def remove_repeat_chars(s):
    if len(s) <= 45:
        return s
    start = 45
    end = min(67, len(s))
    substring = s[start:end]
    chars_to_remove = set([char for char in substring if substring.count(char) > 1])
    result = []
    for i, char in enumerate(s):
        if i < start or i >= end or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)