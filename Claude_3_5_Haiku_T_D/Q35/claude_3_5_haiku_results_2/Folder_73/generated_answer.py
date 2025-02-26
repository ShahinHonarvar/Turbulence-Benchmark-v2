def remove_repeat_chars(s):
    if len(s) <= 11:
        return s
    substring = s[11:76]
    repeat_chars = set()
    seen_chars = set()
    for char in substring:
        if char in seen_chars:
            repeat_chars.add(char)
        seen_chars.add(char)
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
    return result