def filter_chars(s: str) -> str:
    chars_to_remove = []
    for i in range(138, 921):
        if '6' <= s[i] <= 'A':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s