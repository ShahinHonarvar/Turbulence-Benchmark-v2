def filter_chars(s: str) -> str:
    chars_to_remove = set()
    for i in range(219, 403):
        char = s[i]
        if '*' < char < '7':
            chars_to_remove.add(char)
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s