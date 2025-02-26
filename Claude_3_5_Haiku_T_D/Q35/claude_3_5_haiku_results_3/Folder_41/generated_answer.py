def remove_repeat_chars(s):
    if len(s) <= 4:
        return s
    substring = s[4:8]
    repeat_chars = set()
    for char in substring:
        if substring.count(char) > 1 and char not in repeat_chars:
            repeat_chars.add(char)
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
        elif s.index(char) < 4 or s.index(char) >= 8:
            result.append(char)
    return ''.join(result)