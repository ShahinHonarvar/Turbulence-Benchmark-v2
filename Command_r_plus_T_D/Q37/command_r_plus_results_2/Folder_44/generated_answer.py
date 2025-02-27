def filter_chars(s: str) -> str:
    chars_to_remove = []
    for i in range(21, 44):
        if '+' <= s[i] <= '8':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s