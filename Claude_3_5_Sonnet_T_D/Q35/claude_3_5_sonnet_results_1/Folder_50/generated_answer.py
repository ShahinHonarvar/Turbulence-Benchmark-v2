def remove_repeat_chars(s):
    if len(s) <= 14:
        return s
    start = 14
    end = min(76, len(s))
    chars_to_remove = set()
    for i in range(start, end):
        if s[i] in s[start:i] or s[i] in s[i + 1:end]:
            chars_to_remove.add(s[i])
    result = s[:start]
    for char in s[start:]:
        if char not in chars_to_remove:
            result += char
    return result