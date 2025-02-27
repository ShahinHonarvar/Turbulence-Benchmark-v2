def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[50:74]) & set(s[:49])
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
    return result