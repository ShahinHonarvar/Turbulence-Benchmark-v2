def filter_chars(s: str) -> str:
    result = ''
    for i in range(len(s)):
        if i >= 14 and i < 75:
            if ord('9') < ord(s[i]) < ord('K'):
                continue
        result += s[i]
    return result