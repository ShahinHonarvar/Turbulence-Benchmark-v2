def remove_repeat_chars(s):
    if len(s) < 99:
        return s
    substring = s[33:99]
    seen_chars = set()
    repeated_chars = set()
    for char in substring:
        if char in seen_chars:
            repeated_chars.add(char)
        else:
            seen_chars.add(char)
    result = []
    for char in s:
        if char not in repeated_chars:
            result.append(char)
    return ''.join(result)