def remove_repeat_chars(s: str) -> str:
    seen_chars = set()
    chars_to_remove = set()
    for i in range(60, 200):
        if s[i] in seen_chars:
            chars_to_remove.add(s[i])
        seen_chars.add(s[i])
    result = ''
    for char in s[60:200]:
        if char not in chars_to_remove:
            result += char
    return s[:60] + result + s[200:]