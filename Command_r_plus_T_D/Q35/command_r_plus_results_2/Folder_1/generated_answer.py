def remove_repeat_chars(s: str) -> str:
    repeat_chars = set()
    for i in range(17, 88):
        if s[i] in s[17:i] or s[i] in s[i + 1:88]:
            repeat_chars.add(s[i])
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
    return result