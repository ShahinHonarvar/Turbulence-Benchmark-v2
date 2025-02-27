def remove_repeat_chars(s: str) -> str:
    seen_chars = set()
    chars_to_remove = set()
    for i in range(len(s)):
        if i >= 20 and i < 43 and (s[i] in seen_chars):
            chars_to_remove.add(s[i])
        elif i >= 20 and i < 43:
            seen_chars.add(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s