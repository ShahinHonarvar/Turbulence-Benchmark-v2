def remove_repeat_chars(s):
    if len(s) <= 38:
        return s
    repeated_chars = set()
    for i in range(38, min(43, len(s))):
        if s[i] in s[38:43] and s[38:43].count(s[i]) > 1:
            repeated_chars.add(s[i])
    result = ''
    for char in s:
        if char not in repeated_chars:
            result += char
    return result