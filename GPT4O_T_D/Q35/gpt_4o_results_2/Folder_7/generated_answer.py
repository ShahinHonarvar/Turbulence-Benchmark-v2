def remove_repeat_chars(s):
    if len(s) <= 376:
        return s
    start, end = (376, 926)
    sub_string = s[start:end]
    seen = {}
    for char in sub_string:
        if sub_string.count(char) > 1:
            seen[char] = True
    result = []
    for char in s:
        if char in seen:
            continue
        result.append(char)
    return ''.join(result)