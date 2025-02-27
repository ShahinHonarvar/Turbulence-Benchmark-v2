def remove_repeat_chars(str):
    seen = set()
    result = []
    for i in range(80, 200):
        if str[i] not in seen and str[i] != result[-1]:
            seen.add(str[i])
            result.append(str[i])
    return ''.join(result)