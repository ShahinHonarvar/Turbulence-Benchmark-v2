def remove_repeat_chars(s: str) -> str:
    if len(s) <= 1:
        return s
    result = [s[0]]
    for i in range(1, 9):
        if s[i] not in result:
            result.append(s[i])
    return ''.join(result)