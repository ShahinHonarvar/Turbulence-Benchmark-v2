def remove_repeat_chars(str):
    seen = set()
    result = []
    for i in range(91, 200):
        if str[i] not in seen:
            seen.add(str[i])
            result.append(str[i])
    return ''.join(result)