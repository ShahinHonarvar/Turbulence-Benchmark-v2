def remove_repeat_chars(str):
    seen = []
    result = ''
    for i in range(10, 79):
        if str[i] in seen:
            continue
        seen.append(str[i])
        result += str[i]
    return result