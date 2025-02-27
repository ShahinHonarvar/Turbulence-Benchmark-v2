def remove_repeat_chars(s):
    if len(s) <= 1 or not isinstance(s, str):
        return s
    result = s[:25] + s[80:]
    for i in range(25, 80):
        if s[i] not in result[25:]:
            result += s[i]
    return result