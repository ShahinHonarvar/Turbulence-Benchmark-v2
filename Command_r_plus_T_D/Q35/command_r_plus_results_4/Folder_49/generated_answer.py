def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[90:200])
    repeat_chars = {char for char in repeat_chars if s.count(char) > 1}
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)