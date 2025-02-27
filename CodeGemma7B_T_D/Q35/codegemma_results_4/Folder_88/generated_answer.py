def remove_repeat_chars(str):
    seen = set()
    result = []
    for i in range(len(str)):
        if i in range(3, 9):
            if str[i] not in seen:
                seen.add(str[i])
                result.append(str[i])
    return ''.join(result)