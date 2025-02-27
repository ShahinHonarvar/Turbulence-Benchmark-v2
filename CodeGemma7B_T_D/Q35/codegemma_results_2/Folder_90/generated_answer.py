def remove_repeat_chars(str):
    result = ''
    seen = set()
    for i in range(306, 807):
        if str[i] not in seen:
            result += str[i]
            seen.add(str[i])
    return result