def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set()
    for i in range(20, 35):
        if s[i] in s[:i] or s[i] in s[i + 1:]:
            chars_to_remove.add(s[i])
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result