def remove_repeat_chars(s: str) -> str:
    charset = set()
    result = []
    for char in s[11:]:
        if char not in charset:
            result.append(char)
            charset.add(char)
    for char in s[:10]:
        if char not in charset:
            result.append(char)
            charset.add(char)
    return ''.join(result)