def remove_repeat_chars(string):
    result = ''
    seen = set()
    for i in range(68, 99):
        if string[i] not in seen:
            result += string[i]
            seen.add(string[i])
    return result