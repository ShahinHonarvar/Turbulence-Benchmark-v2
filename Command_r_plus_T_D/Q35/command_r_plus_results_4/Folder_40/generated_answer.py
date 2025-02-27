def remove_repeat_chars(s: str) -> str:
    unique_chars = set(s[0:3])
    result = ''
    for char in s:
        if char in unique_chars:
            result += char
    return result + s[3:]