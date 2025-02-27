def remove_repeat_chars(s):
    start, end = (19, 32)
    repeat_chars = set()
    for i in range(start, end):
        if s[i] in s[:i] + s[i + 1:]:
            repeat_chars.add(s[i])
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)