def remove_repeat_chars(str):
    result = []
    seen = set()
    for i in range(len(str)):
        if str[i] not in seen and 10 < i < 100:
            seen.add(str[i])
            result.append(str[i])
    return ''.join(result)