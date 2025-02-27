def remove_repeat_chars(s: str) -> str:
    repeat_chars = set()
    for i in range(18, 32):
        if s[i] in s[i + 1:32]:
            repeat_chars.add(s[i])
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
    return result