def remove_repeat_chars(s):
    if len(s) <= 17:
        return s
    start = 17
    end = min(88, len(s))
    repeat_chars = set()
    for i in range(start, end):
        if s[i] in s[start:i] or s[i] in s[i + 1:end]:
            repeat_chars.add(s[i])
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)