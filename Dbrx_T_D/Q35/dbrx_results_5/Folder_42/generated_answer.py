def remove_repeat_chars(s: str) -> str:
    used_chars = set()
    result = s[:18] + s[60:]
    for char in s[18:60]:
        if char not in used_chars:
            result += char
            used_chars.add(char)
    return result