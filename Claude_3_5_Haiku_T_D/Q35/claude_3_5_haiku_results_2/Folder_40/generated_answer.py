def remove_repeat_chars(s):
    if len(s) <= 4:
        return s
    repeated_chars = set()
    for char in s[1:3]:
        if s[1:3].count(char) > 1 and char not in repeated_chars:
            repeated_chars.add(char)
    result = []
    for char in s:
        if char not in repeated_chars:
            result.append(char)
    return ''.join(result)