def remove_repeat_chars(str):
    seen = set()
    result = []
    for i in range(10, 79):
        if str[i] not in seen:
            result.append(str[i])
            seen.add(str[i])
    return ''.join(result)