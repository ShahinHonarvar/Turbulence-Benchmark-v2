def remove_repeat_chars(s):
    if len(s) <= 43:
        return s
    repeated_chars = set()
    for i in range(21, 43):
        if s[i] in s[21:43] and s[i] not in repeated_chars:
            repeated_chars.add(s[i])
    result = []
    for char in s:
        if char not in repeated_chars:
            result.append(char)
    return ''.join(result)