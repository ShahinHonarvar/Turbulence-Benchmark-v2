def remove_repeat_chars(s: str) -> str:
    result = ''
    for i in range(33, 100):
        if s[i] not in result:
            result += s[i]
    return result