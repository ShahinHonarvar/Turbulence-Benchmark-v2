def remove_repeat_chars(s):
    seen = set()
    repeat_chars = set()
    result = []
    for char in s[:33]:
        result.append(char)
    for char in s[33:78]:
        if char in seen:
            repeat_chars.add(char)
        seen.add(char)
    for char in s[78:]:
        if char not in repeat_chars:
            result.append(char)
    for char in s[33:78]:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)