def remove_repeat_chars(s):
    if len(s) <= 27:
        return s
    substring = s[28:96]
    repeat_chars = set()
    seen_chars = set()
    for char in substring:
        if char in seen_chars:
            repeat_chars.add(char)
        else:
            seen_chars.add(char)
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)