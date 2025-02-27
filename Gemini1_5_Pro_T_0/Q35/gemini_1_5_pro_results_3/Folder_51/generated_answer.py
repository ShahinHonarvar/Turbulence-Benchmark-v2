def remove_repeat_chars(s):
    seen_chars = set()
    repeat_chars = set()
    for i in range(7, 9):
        if s[i] in seen_chars:
            repeat_chars.add(s[i])
        else:
            seen_chars.add(s[i])
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
    return result