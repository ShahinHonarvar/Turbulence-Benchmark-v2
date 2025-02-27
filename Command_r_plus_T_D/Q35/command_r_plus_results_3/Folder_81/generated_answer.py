def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[20:200])
    unique_chars = set(s[:20])
    unique_chars.update(s[200:])
    unique_chars = unique_chars - repeat_chars
    result = []
    for char in s:
        if char in unique_chars:
            result.append(char)
    return ''.join(result)