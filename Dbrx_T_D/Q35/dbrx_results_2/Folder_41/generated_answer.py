def remove_repeat_chars(s: str) -> str:
    result = ''
    seen_chars = set()
    for char in s[3:8]:
        if char in seen_chars:
            seen_chars.add(char)
        elif char in s[3:9]:
            result = result.replace(char, '')
    for char in s[:3] + s[8:]:
        result += char
    return result