def remove_repeat_chars(s):
    start, end = (409, 502)
    repeat_chars = set()
    for i in range(start + 1, end):
        if s[i] in s[start:i]:
            repeat_chars.add(s[i])
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)