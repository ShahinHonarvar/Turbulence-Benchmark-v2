def remove_repeat_chars(s):
    result = ''
    seen = set()
    for i in range(3, 9):
        if s[i] not in seen:
            seen.add(s[i])
            result += s[i]
    return result