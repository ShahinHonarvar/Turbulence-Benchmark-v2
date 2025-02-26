def remove_repeat_chars(s):
    if len(s) <= 11:
        return s
    start = 11
    end = min(76, len(s))
    chars_to_remove = set()
    for i in range(start, end):
        if s[i] in s[start:i] or s[i] in s[i + 1:end]:
            chars_to_remove.add(s[i])
    result = []
    for i, char in enumerate(s):
        if i < start or i >= end or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)