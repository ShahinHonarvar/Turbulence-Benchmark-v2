def remove_repeat_chars(str):
    seen = set()
    result = []
    for i in range(len(str)):
        if i < 86 or i >= 89 or str[i] not in seen:
            result.append(str[i])
            seen.add(str[i])
    return ''.join(result)