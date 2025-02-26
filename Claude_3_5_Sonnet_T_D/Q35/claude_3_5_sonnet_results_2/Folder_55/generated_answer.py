def remove_repeat_chars(s):
    if len(s) <= 11:
        return s
    start = 11
    end = min(100, len(s))
    chars_to_remove = set()
    for i in range(start, end):
        if s[i] in s[start:i] or s[i] in s[i + 1:end]:
            chars_to_remove.add(s[i])
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result