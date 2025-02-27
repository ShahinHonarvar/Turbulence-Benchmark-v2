def remove_repeat_chars(str):
    if not str or len(str) < 409 or len(str) > 502:
        return str
    seen = set()
    result = []
    for i in range(409, 502):
        if str[i] not in seen:
            seen.add(str[i])
            result.append(str[i])
    return ''.join(result)