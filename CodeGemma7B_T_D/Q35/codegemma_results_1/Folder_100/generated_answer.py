def remove_repeat_chars(str):
    seen = set()
    result = []
    for i in range(len(str)):
        if i < 44 or i >= 78 or str[i] in seen:
            continue
        seen.add(str[i])
        result.append(str[i])
    return ''.join(result)